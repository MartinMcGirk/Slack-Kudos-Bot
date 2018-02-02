import os
import urllib

from botocore.vendored import requests

SLACK_ROOT = "https://slack.com/api/"
POST_MESSAGE = "chat.postMessage"
GET_USERS = 'users.list'
AUTH_TEST = 'auth.test'

BOT_TOKEN = os.environ.get('BOT_TOKEN')


def send_message_to_slack(channel, message):
    data = urllib.parse.urlencode(
        (
            ("token", BOT_TOKEN),
            ("channel", channel),
            ("text", message)
        )
    )
    data = data.encode("ascii")
    request = urllib.request.Request(
        SLACK_ROOT + POST_MESSAGE,
        data=data,
        method="POST"
    )
    request.add_header(
        "Content-Type",
        "application/x-www-form-urlencoded"
    )

    urllib.request.urlopen(request).read()


def get_from_slack(endpoint):
    url = SLACK_ROOT + endpoint + '?token=' + BOT_TOKEN
    return requests.get(url).json()