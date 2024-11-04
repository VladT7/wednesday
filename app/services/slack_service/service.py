from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackService:
    def __init__(self, token):
        self.client = WebClient(token=token)

    def post_message(self, channel, text):
        try:
            self.client.chat_postMessage(channel=channel, text=text)
        except SlackApiError as e:
            print(f"Error posting message: {e.response['error']}")
            raise

    def handle_mention(self, event):
        channel = event["channel"]
        self.post_message(channel, "I'm here! Ask me about Monday.com boards.")
