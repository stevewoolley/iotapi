from __future__ import print_function

import boto3
import json

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
    response = table.get_item(
        Key={
            'domain': event['domain'],
            'thing': event['thing']
        }
    )
    if 'Item' in response:
        client = boto3.client('iot-data', region_name='us-east-1')
        response = client.get_thing_shadow(thingName=event['thing'])
        body = response["payload"]
        return json.loads(body.read())
    else:
        return _error(NOT_FOUND, 'Thing not found')


