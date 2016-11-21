from __future__ import print_function

import boto3

BAD_REQUEST = 'BadRequest'
FORBIDDEN = 'Forbidden'
NOT_FOUND = 'NotFound'
INTERNAL_SERVER_ERROR = 'InternalServerError'


def _error(status, msg):
    """ Utility to handle custom errors (see response mapping) """
    raise Exception("[{}] {}".format(status, msg))


def show(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('iot-domains')
    if 'domainName' in event:
        response = table.get_item(
            Key={'domain': event['domainName']}
        )
    if 'Item' in response:
        return response['Item']
    else:
        return _error(NOT_FOUND, 'Domain not found')


def showAll(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('iot-domains')

    response = table.scan()
    if 'Items' in response:
        return response['Items']
    else:
        return _error(NOT_FOUND, 'No domains found')
