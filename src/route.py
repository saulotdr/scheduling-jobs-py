import constants
import response
import validation

from json import dumps
from re import findall
from datetime import datetime as dt
from fastjsonschema import JsonSchemaException
from logging import getLogger
from flask import Flask, request

''' Module logger configuration '''
logger = getLogger(__name__)

''' Flask configuration '''
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

window = dict()


@app.route('/api/jobs', methods=['POST'])
def process_jobs_array():
    logger.debug('Headers: {0}'.format(request.headers))
    logger.debug('Data: {0}'.format(dumps(request.json,
                                          indent=4,
                                          ensure_ascii=False)))
    try:
        validate_input()
    except JsonSchemaException as e:
        logger.debug('JsonSchemaException raised: {0}'.format(e.message))
        return response.error()
    fill_window()
    fill_payload()
    return response.ok({'r': 'Ok'})


def validate_input():
    headers, payload = request.headers, request.json
    if constants.WINDOW_BEGIN not in headers or not headers[constants.WINDOW_BEGIN]:
        raise JsonSchemaException('Header must contains "JANELA_INICIO"')
    if constants.WINDOW_END not in headers or not headers[constants.WINDOW_END]:
        raise JsonSchemaException('Header must contains "JANELA_FIM"')
    if payload is None or not payload:
        raise JsonSchemaException('Payload must not be empty')
    validation.schema(payload)
    # validation.window(headers)


def fill_window():
    headers = request.headers
    window['begin_ts'] = dt.strptime(
        headers[constants.WINDOW_BEGIN], '%Y-%m-%d %H:%M:%S').timestamp()
    window['end_ts'] = dt.strptime(
        headers[constants.WINDOW_END], '%Y-%m-%d %H:%M:%S').timestamp()
    window['duration'] = window['end_ts'] - window['begin_ts']
    logger.debug(dumps(window, indent=4, ensure_ascii=False))


def fill_payload():
    payload = request.json
    for job in payload:
        job['timestamp'] = int(
            dt.strptime(job['Data Máxima de conclusão'],
            '%Y-%m-%d %H:%M:%S').timestamp())
        # create a timestamp with the job duration
        # and store it in a key-value pair.
        # regex will omit the string 'horas' from the string.
        job['duration'] = int(
            findall(r"(?![horas])\w+", job['Tempo estimado'])[0]) * 60 * 60
    logger.debug(dumps(payload, indent=4, ensure_ascii=False))
