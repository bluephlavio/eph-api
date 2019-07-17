import json
from eph import get


def main(event, context):
    params = json.loads(event['body'])
    objs = params['objs']
    dates = params['dates']

    data = get(399, dates)

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
