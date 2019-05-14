import json


def vectors(event, context):

    params = json.loads(event['body'])
    objs = params['objs']
    dates = params['dates']

    body = {
        "objs": objs,
        "dates": dates
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
