import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import requests

load_dotenv()

app = Flask(__name__)

slack_token = os.environ["SLACK_BOT_TOKEN"]
slack_client = WebClient(token=slack_token)


def post_message(channel, text):
    try:
        slack_client.chat_postMessage(channel=channel, text=text)
    except SlackApiError as e:
        print(f"Error posting message: {e.response['error']}")


@app.route("/slack/events", methods=["POST"])
def slack_events():
    data = request.json

    # Slack requires a challenge verification for URL validation
    if "challenge" in data:
        return jsonify({"challenge": data["challenge"]})

    # Process events (like mentions or commands)
    if "event" in data:
        event = data["event"]

        # Respond to messages where the bot is mentioned
        if event.get("type") == "app_mention":
            channel = event["channel"]
            text = event["text"]

            # Handle the message or command
            # if "boards" in text:
            #     boards = get_monday_boards()
            #     message = "Here are your Monday.com boards:\n"
            #     for board in boards:
            #         message += f"- {board['name']} (ID: {board['id']})\n"
            #     post_message(channel, message)
            # else:
            post_message(channel, "I'm here! Ask me about Monday.com boards.")

    return "", 200
