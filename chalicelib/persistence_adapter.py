store = {}


def add_points_to_user(slack_message):
    user_id = slack_message.recipient
    points = slack_message.count_emojis_in_message()
    user_total = store.get(user_id, 0) + points
    store[user_id] = user_total
    return user_total


def get_user_points():
    return store