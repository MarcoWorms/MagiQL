# MagiQL

Telegram bot that can send requests made with natural language to a GraphQL endpoint and process responses.

Made with https://github.com/MarcoWorms/RefactorGPT

[![](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

## Requirements

You need to have [Docker](https://docs.docker.com/engine/install/) installed on your machine.

## Usage

1. Build the Docker image (add your openAI and telegram keys, and also graphql endpoint): `docker build --build-arg GRAPHQL_ENDPOINT='your-graphql-endpoint' --build-arg OPENAI_API_KEY='your_openai_api_key' --build-arg TELEGRAM_BOT_TOKEN='your_telegram_bot_token' -t telegram-bot .`
2. Run the Docker container: `docker run telegram-bot`

- `/query insert your question here` is the main thing
- `/query_info` provides documentation on the endpoint schema (if you don't know the schemas you might ask for impossible queries and it will throw error saying it can't do it)

## Examples

![image](https://github.com/MarcoWorms/MagiQL/assets/7863230/dbbeadc9-5b86-4746-b23e-7ebb3707521a)

![image](https://github.com/MarcoWorms/MagiQL/assets/7863230/99b3228e-d775-4633-b579-78499e3eca8c)
