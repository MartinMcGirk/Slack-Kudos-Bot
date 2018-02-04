from chalicelib.global_constants import EMOJI


class SlackMessage:
    def __init__(self, sender, recipients, message, channel):
        self.sender = sender
        self.recipients = recipients
        self.message = message
        self.channel = channel

    def count_emojis_in_message(self):
        return self.message.count(EMOJI)