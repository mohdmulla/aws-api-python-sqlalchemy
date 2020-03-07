"""
This is a sample code demonstrating using SQLALCHEMY to retrieve data. This code has been used to create with aws lambda. 
@author : Mulla Mohammed
"""

from lambda_db import session, Science
from utils import AlchemyEncoder

import json
import datetime

params = ['instrument_id', 'data_level', 'version', 'start_date', 'end_date']


def lambda_handler(event, context):
    """Main lambda function where the parameters will be accepted"""
    filters = {}
    start_date, end_date = None, None

    parameters = event['params']['querystring']

    for param in params:
        try:
            if param == 'version':
                filters.update({param: int(parameters[param])})
            elif param == 'start_date':
                start_date = datetime.datetime.strptime(parameters[param],
                                                        '%Y-%m-%d')
            elif param == 'end_date':
                end_date = datetime.datetime.strptime(parameters[param], '%Y-%m-%d')
            else:
                filters.update({param: parameters[param]})
        except KeyError:
            continue
        except TypeError:
            continue
        except ValueError as e:
            return {
                'statusCode': 500,
                'body': str(e)
            }

    if start_date is not None and end_date is not None:
        result = session.query(Science).filter_by(**filters).filter(
            Science.timetag >= start_date, Science.timetag <= end_date).all()
    elif start_date is None and end_date is None:
        result = session.query(Science).filter_by(**filters).all()
    else:
        if start_date is None:
            subquery = Science.timetag <= end_date

        if end_date is None:
            subquery = Science.timetag >= start_date

        result = session.query(Science).filter_by(**filters).filter(
            subquery).all()

    json_result = json.dumps(result, cls=AlchemyEncoder)
    return {
        'statusCode': 200,
        'body': json_result
    }


# To run locally
# event['queryStringParameters'] = {
#         # 'instrument_id': 'emu',
#         # 'version': 0,
#         'start_date': '2018-12-18',
#         'end_date': '2019-01-29'
#     }
# lambda_handler(event, None)






