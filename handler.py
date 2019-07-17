import json
from eph import vec


def vectors(event, context):

    params = json.loads(event['body'])
    objs = params['objs']
    dates = params['dates']

    data = vec(399)

    body = {
        "objs": objs,
        "dates": dates,
        "data": data
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
