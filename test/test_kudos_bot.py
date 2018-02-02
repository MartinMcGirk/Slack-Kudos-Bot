from unittest import TestCase

from chalicelib.kudos_bot import handle_message


class KudosBotTestCase(TestCase):

    def test_handle_message_responds_to_verification_challenge(self):
        mockMessage = {
            'challenge': '1234'
        }
        response = handle_message(mockMessage)
        self.assertEquals('1234', response)

    def test_handle_message_ignores_bot_events(self):
        mockMessage = {
            'event': {
                'bot_id': 'test'
            }
        }
        response = handle_message(mockMessage)
        self.assertIsNone(response)