from __future__ import print_function

import boto3
from boto3.dynamodb.conditions import Key, Attr

BAD_REQUEST = 'BadRequest'
FORBIDDEN = 'Forbidden'
NOT_FOUND = 'NotFound'
INTERNAL_SERVER_ERROR = 'InternalServerError'


def _error(status, msg):
    """ Utility to handle custom errors (see response mapping) """
    raise Exception("[{}] {}".format(status, msg))


def show(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('iot-memberships')
    if 'domain' not in event:
        return _error(BAD_REQUEST, 'Must specify domain')
    if 'username' not in event:
        return _error(BAD_REQUEST, 'Must specify username')
    response = table.get_item(
        Key={
            'domain': event['domain'],
            'username': event['username']
        }
    )
    if 'Item' in response:
        table2 = dynamodb.Table('iot-users')
        response2 = table2.get_item(
            Key={
                'username': event['username']
            }
        )
        return response2['Item']
    else:
        return _error(NOT_FOUND, 'User not found')


def showAll(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('iot-memberships')
    if 'domain' not in event:
        return _error(BAD_REQUEST, 'Must specify domain')
    response = table.query(
        KeyConditionExpression=Key('domain').eq(event['domain'])
    )
    return response['Items']
