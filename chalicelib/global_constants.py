import os

EMOJI = os.environ.get('EMOJI', ':taco:')
EMOJI_PLURAL = os.environ.get('EMOJI_PLURAL', 'tacos')
MAX_POINTS_PER_USER_PER_DAY = int(os.environ.get('MAX_POINTS_PER_USER_PER_DAY', 5))
BOT_NAME = os.environ.get('BOT_NAME', 'KudosBot')
