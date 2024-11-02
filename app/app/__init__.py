import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import requests

load_dotenv()

slack_token = os.environ["SLACK_BOT_TOKEN"]
monday_token = os.environ["MONDAY_API_TOKEN"]
slack_client = WebClient(token=slack_token)


def get_monday_boards():
    url = "https://api.monday.com/v2"
    headers = {"Authorization": monday_token}
    query = "{ boards { id name } }"
    response = requests.post(url, json={"query": query}, headers=headers)
    if response.status_code == 200:
        return response.json()["data"]["boards"]
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")


def post_message(channel, text):
    try:
        slack_client.chat_postMessage(channel=channel, text=text)
    except SlackApiError as e:
        print(f"Error posting message: {e.response['error']}")


if __name__ == "__main__":
    # boards = get_monday_boards()
    message = "Here are your Monday.com boards:\n"
    # for board in boards:
    #     message += f"- {board['name']} (ID: {board['id']})\n"
    post_message("#testing", message)
