# Telegram Bot with GPT-4 and GraphQL

This is a Telegram bot that can send requests to a GraphQL endpoint and process responses with GPT-4.

## Requirements

You need to have Docker installed on your machine.

## Usage

1. Build the [Docker](https://docs.docker.com/engine/install/) image (add your openAI and telegram keys): `docker build --build-arg GRAPHQL_ENDPOINT='https://api.thegraph.com/subgraphs/name/messari/yearn-v2-ethereum/graphql' --build-arg OPENAI_API_KEY='your_openai_api_key' --build-arg TELEGRAM_BOT_TOKEN='your_telegram_bot_token' -t telegram-bot .`
2. Run the Docker container: `docker run telegram-bot`