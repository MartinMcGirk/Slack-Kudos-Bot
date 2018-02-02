import re
from chalicelib.slack_message import SlackMessage


MENTION_REGEX = '^<@(|[WU].+?)>(.*)'


def parse_message(event):
    if event['type'] == 'message' and not 'subtype' in event:
        sender_user_id = event['user']
        recipient_user_id, message = extract_recipient_and_message(event['text'])
        return SlackMessage(sender_user_id, recipient_user_id, message, event['channel'])
    return None


def extract_recipient_and_message(message_text):
    matches = re.search(MENTION_REGEX, message_text)
    if matches:
        # the first group contains the username, the second group contains the remaining message
        return (matches.group(1), matches.group(2).strip()) if matches else (None, None)
    else:
        return None, message_text
