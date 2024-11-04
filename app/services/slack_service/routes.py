from flask import Blueprint, request, jsonify
from .service import SlackService
import os

slack_routes = Blueprint("slack_routes", __name__)
slack_service = SlackService(os.environ["SLACK_BOT_TOKEN"])


@slack_routes.route("/slack/events", methods=["POST"])
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
            slack_service.handle_mention(event)

    return "", 200
