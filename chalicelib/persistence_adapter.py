import boto3
from collections import Counter
from datetime import datetime, timedelta

import logging
from boto3.dynamodb.conditions import Key


DYNAMODB = boto3.client('dynamodb')
dynresource = boto3.resource('dynamodb')
table = dynresource.Table('emoji_log')


def add_points_to_user(slack_message, recipient, points):
    for _ in range(points):
        now = datetime.now()
        now.isoformat()
        DYNAMODB.put_item(TableName='emoji_log', Item={
            'sender': {'S': slack_message.sender},
            'recipient': {'S': recipient},
            'datetime_given': {'S': str(now)},
            'channel': {'S': slack_message.channel}
        })


def get_user_points():
    results = table.scan(TableName='emoji_log', ProjectionExpression='recipient')['Items']
    recipients = [recipient['recipient'] for recipient in results]
    return Counter(recipients).most_common()


def get_number_of_points_given_so_far_today(user_id):
    start_of_day = datetime.now().date()
    end_of_day = start_of_day + timedelta(1)
    start = start_of_day.isoformat()
    end = end_of_day.isoformat()

    results = table.query(
        TableName='emoji_log',
        KeyConditionExpression=Key('sender').eq(user_id) & Key('datetime_given').between(start, end)
    )['Items']

    return len(results)