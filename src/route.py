import constants
import response
import validation

from json import dumps
from fastjsonschema import JsonSchemaException
from logging import getLogger
from flask import Flask, request

''' Module logger configuration '''
logger = getLogger(__name__)

''' Flask configuration '''
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = constants.PRETTY_PRINT


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
    return response.ok({'r': 'Ok'})


def validate_input():
    headers, payload = request.headers, request.json
    if 'JANELA_INICIO' not in headers or not headers['JANELA_INICIO']:
        raise JsonSchemaException('Header must contain "JANELA_INICIO"')
    if 'JANELA_FIM' not in headers or not headers['JANELA_FIM']:
        raise JsonSchemaException('Header must contain "JANELA_FIM"')
    if payload is None or not payload:
        raise JsonSchemaException('Payload must not be empty')
    validation.schema(payload)
    # validation.window(headers)
