import json
import eph
import pandas as pd

def handler(event, context):
    params = json.loads(event['body'])
    objs = params['objs']
    dates = params['dates']
    jplparams = params['jplparams']

    data = eph.get(objs, dates=dates, **jplparams)
    df = data.to_pandas()

    body = {
        "objs": objs,
        "dates": dates,
        "data": df.to_json(orient='records')
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
