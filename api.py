import json
import eph
import pandas as pd
from datetime import datetime


def handler(event, context):
    try:
        params = json.loads(event['body'])
        objs = params['objs']
        dates = params.get('dates',
                        datetime.now().strftime('%Y-%m-%d %H:%M'))
        orient = params.get('orient', 'records')
        jplparams = params.get('jplparams', {})

        table = eph.get(objs, dates=dates, **jplparams)

        data = json.loads(table.to_pandas().to_json(orient=orient))

        response = {"statusCode": 200, "body": json.dumps({"data": data})}
    except:
        response = {"statusCode": 500, "body": json.dumps({"error": "Internal Server Error"})}
    return response