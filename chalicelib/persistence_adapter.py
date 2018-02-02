import boto3
from collections import Counter
from datetime import datetime



DYNAMODB = boto3.client('dynamodb')


def add_points_to_user(slack_message):
    now = datetime.now()
    now.isoformat()

    DYNAMODB.put_item(TableName='emoji_log', Item={
        'sender': {'S': slack_message.sender},
        'recipient': {'S': slack_message.recipient},
        'datetime_given': {'S': str(now)},
        'channel': {'S': slack_message.channel}
    })


def get_user_points():
    results = DYNAMODB.scan(TableName='emoji_log', ProjectionExpression='recipient')['Items']
    recipients = [recipient['recipient']['S'] for recipient in results]
    return Counter(recipients).most_common()
