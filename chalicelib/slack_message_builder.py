import re
from chalicelib.slack_message import SlackMessage


MENTION_REGEX = '<@(|[WU].+?)>'


def parse_message(event):
    if event['type'] == 'message' and not 'subtype' in event:
        sender_user_id = event['user']
        recipient_user_id = _extract_recipient_from_message(event['text'])
        return SlackMessage(sender_user_id, recipient_user_id, event['text'], event['channel'])
    return None


def _extract_recipient_from_message(message_text):
    matches = re.findall(MENTION_REGEX, message_text)
    return matches if matches else None
    # if matches:
    #     # the first group contains the username, the second group contains the remaining message
    #     return (matches.group(1)) if matches else (None)
    # else:
    #     return None
