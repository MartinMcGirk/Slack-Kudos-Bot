from unittest import TestCase

from chalicelib.slack_message_builder import parse_message


class SlackMessageBuilderTestCase(TestCase):

    def test_returns_none_if_event_not_a_message(self):
        mockEvent = {
            'type': 'some_other_type'
        }
        response = parse_message(mockEvent)
        self.assertIsNone(response)

    def test_can_parse_message_correctly_with_no_recipient(self):
        mockEvent = {
            'type': 'message',
            'user': 'User1',
            'text': 'This is a message',
            'channel': '#general'
        }
        parsed_message = parse_message(mockEvent)
        self.assertEquals('User1', parsed_message.sender)
        self.assertIsNone(parsed_message.recipient)
        self.assertEquals('This is a message', parsed_message.message)
        self.assertEquals('#general', parsed_message.channel)

    def test_can_parse_message_correctly_with_a_recipient(self):
        mockEvent = {
            'type': 'message',
            'user': 'User1',
            'text': '<@User2> This is a message',
            'channel': '#general'
        }
        parsed_message = parse_message(mockEvent)
        self.assertEquals('User1', parsed_message.sender)
        self.assertEquals('User2', parsed_message.recipient)
        self.assertEquals('<@User2> This is a message', parsed_message.message)
        self.assertEquals('#general', parsed_message.channel)

    def test_can_parse_message_correctly_with_a_recipientat_the_end(self):
        mockEvent = {
            'type': 'message',
            'user': 'User1',
            'text': 'This is a message for <@User2>',
            'channel': '#general'
        }
        parsed_message = parse_message(mockEvent)
        self.assertEquals('User1', parsed_message.sender)
        self.assertEquals('User2', parsed_message.recipient)
        self.assertEquals('This is a message for <@User2>', parsed_message.message)
        self.assertEquals('#general', parsed_message.channel)
