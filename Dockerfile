# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Pass environment variables
ARG GRAPHQL_ENDPOINT
ARG OPENAI_API_KEY
ARG TELEGRAM_BOT_TOKEN
ENV GRAPHQL_ENDPOINT=$GRAPHQL_ENDPOINT
ENV OPENAI_API_KEY=$OPENAI_API_KEY
ENV TELEGRAM_BOT_TOKEN=$TELEGRAM_BOT_TOKEN

# Run bot.py when the container launches
CMD ["python", "bot.py"]