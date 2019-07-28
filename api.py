try:
    import unzip_requirements
except ImportError:
    pass

import json
import eph
import pandas as pd
from datetime import datetime
import logging

logger = logging.getLogger()


def handler(event, context):
    response = {"headers": {"Access-Control-Allow-Origin": "*"}}
    try:
        params = json.loads(event['body'])
        objs = params['objs']
        dates = params.get('dates',
                        datetime.now().strftime('%Y-%m-%d %H:%M'))
        orient = params.get('orient', 'records')
        jplparams = params.get('jplparams', {})

        table = eph.get(objs, dates=dates, **jplparams)

        data = json.loads(table.to_pandas().to_json(orient=orient))

        response["statusCode"] = 200
        response["body"] = json.dumps({"data": data})
    except Exception as e:
        logger.error(str(e))
        response["statusCode"] = 500
        response["body"] = json.dumps({"error": str(e)})
    return response
