from unittest import TestCase

from chalicelib.global_constants import EMOJI
from chalicelib.slack_message import SlackMessage


class SlackMessageTestCase(TestCase):

    def test_can_instantiate_slack_message(self):
        recipient = 'User1'
        sender = 'User2'
        message = 'this is a message'
        channel = '#hey_emoji'
        slack_message = SlackMessage(sender, recipient, message, channel)
        self.assertEquals(recipient, slack_message.recipient)
        self.assertEquals(sender, slack_message.sender)
        self.assertEquals(message, slack_message.message)
        self.assertEquals(channel, slack_message.channel)

    def test_can_count_0_emojis_in_message(self):
        recipient = 'User1'
        sender = 'User2'
        message = 'this is a message'
        channel = '#hey_emoji'
        slack_message = SlackMessage(sender, recipient, message, channel)
        self.assertEquals(0, slack_message.count_emojis_in_message())

    def test_can_count_1_emojis_in_message(self):
        recipient = 'User1'
        sender = 'User2'
        message = 'this is a message ' + EMOJI
        channel = '#hey_emoji'
        slack_message = SlackMessage(sender, recipient, message, channel)
        self.assertEquals(1, slack_message.count_emojis_in_message())

    def test_can_count_5_emojis_in_message(self):
        recipient = 'User1'
        sender = 'User2'
        message = 'this is a message ' + EMOJI + EMOJI + EMOJI + EMOJI + EMOJI
        channel = '#hey_emoji'
        slack_message = SlackMessage(sender, recipient, message, channel)
        self.assertEquals(5, slack_message.count_emojis_in_message())

    def test_can_count_emojis_when_anywhere_in_message(self):
        recipient = 'User1'
        sender = 'User2'
        message = 'this is a message ' + EMOJI + EMOJI + ' with emojis interspersed ' + EMOJI
        channel = '#hey_emoji'
        slack_message = SlackMessage(sender, recipient, message, channel)
        self.assertEquals(3, slack_message.count_emojis_in_message())