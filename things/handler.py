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
    table = dynamodb.Table('iot-things')
    if 'domain' not in event:
        return _error(BAD_REQUEST, 'Must specify domain')
    if 'thing' not in event:
        return _error(BAD_REQUEST, 'Must specify thing')
    response = table.query(
        KeyConditionExpression=Key('domain').eq(event['domain']) & Key('thing').eq(event['thing'])
    )
    return response['Items']


def showAll(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('iot-things')
    if 'domain' not in event:
        return _error(BAD_REQUEST, 'Must specify domain')
    response = table.query(
        KeyConditionExpression=Key('domain').eq(event['domain'])
    )
    return response['Items']
