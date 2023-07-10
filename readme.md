# MagiQL

[![](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

![image](https://github.com/MarcoWorms/MagiQL/assets/7863230/3ed88530-fb04-4ecf-a1bf-9f33a902516d)

This is a Telegram bot that can send requests made with natural language to a GraphQL endpoint and process responses.

## Requirements

You need to have [Docker](https://docs.docker.com/engine/install/) installed on your machine.

## Usage

1. Build the Docker image (add your openAI and telegram keys): `docker build --build-arg GRAPHQL_ENDPOINT='https://api.thegraph.com/subgraphs/name/messari/yearn-v2-ethereum/graphql' --build-arg OPENAI_API_KEY='your_openai_api_key' --build-arg TELEGRAM_BOT_TOKEN='your_telegram_bot_token' -t telegram-bot .`
2. Run the Docker container: `docker run telegram-bot`
