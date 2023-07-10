import os
import json
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import openai

# Initialize OpenAI GPT-4
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize GraphQL client
transport = RequestsHTTPTransport(url=os.getenv('GRAPHQL_ENDPOINT'))
client = Client(transport=transport)

# Get GraphQL schema
schema_query = gql("""
query {
  __schema {
    types {
      name
      kind
      description
      fields {
        name
      }
    }
  }
}
""")
schema = client.execute(schema_query)

def query(update: Update, context: CallbackContext) -> None:
    # Get user query from message
    user_query = update.message.text[7:]

    # Request GPT-4 to generate GraphQL query
    gpt_response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        stop=["```"],
        messages=[
            {"role": "user", "content": str(schema)},
            {"role": "user", "content": "User question to transform in GraphQL query using the above schema:\n\n" + user_query},
            {"role": "user", "content": "GraphQL Query: ```graphql\n"},
        ]
    )

    graphql_query = str(gpt_response["choices"][0]["message"]["content"])

    # Execute GraphQL query
    data_query = gql(graphql_query)
    data = client.execute(data_query)

    # Write the raw JSON data to a file
    with open('result.json', 'w') as f:
        json.dump(data, f)

    # Send back the JSON file
    update.message.reply_document(document=open('result.json', 'rb'), reply_to_message_id=update.message.message_id, caption="Query:\n\n" + graphql_query)

def main() -> None:
    updater = Updater(token=os.getenv('TELEGRAM_BOT_TOKEN'))

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("query", query))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()