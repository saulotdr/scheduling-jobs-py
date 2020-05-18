import src.constants as constants
import src.response as response
import src.validation as validation

from datetime import datetime as dt
from fastjsonschema import JsonSchemaException
from flask import Flask, request
from json import dumps
from logging import getLogger
from math import ceil
from operator import itemgetter as get_item
from re import findall

''' Module logger configuration '''
logger = getLogger(__name__)

''' Flask configuration '''
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

window_info = dict()


@app.route(constants.POST_ROUTE, methods=['POST'])
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
    return response.ok(get_jobid_array())


def validate_input():
    headers, payload = request.headers, request.json
    if constants.WINDOW_BEGIN_KEY not in headers or not headers[constants.WINDOW_BEGIN_KEY]:
        raise JsonSchemaException('Header must contains "JANELA_INICIO"')
    if constants.WINDOW_END_KEY not in headers or not headers[constants.WINDOW_END_KEY]:
        raise JsonSchemaException('Header must contains "JANELA_FIM"')
    if payload is None or not payload:
        raise JsonSchemaException('Payload must not be empty')
    validation.validate(payload)


def fill_window():
    headers = request.headers
    window_info['begin_ts'] = int(dt.strptime(
        headers[constants.WINDOW_BEGIN_KEY], '%Y-%m-%d %H:%M:%S').timestamp())
    window_info['end_ts'] = int(dt.strptime(
        headers[constants.WINDOW_END_KEY], '%Y-%m-%d %H:%M:%S').timestamp())
    window_info['duration'] = window_info['end_ts'] - window_info['begin_ts']
    logger.debug(dumps(window_info, indent=4, ensure_ascii=False))


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
            findall(r"(?![hora])\w+", job['Tempo estimado'])[0]) * 3600
    logger.debug(dumps(payload, indent=4, ensure_ascii=False))


def get_jobid_array():
    payload = request.json
    jobs = list()
    for job in payload:
        jobs.append({
            'id': job['ID'],
            'duration': job['duration'],
            'timestamp': job['timestamp']
        })
    jobs_sorted = sorted(jobs, key=lambda k: k['timestamp'])
    logger.debug('Sorted Job array: {0}'
            .format(dumps(jobs_sorted, indent=4, ensure_ascii=False)))

    jobid_array = list()
    windows_len = ceil(window_info['duration'] / constants.WINDOW_DURATION)
    logger.debug('Possible windows: {0}'.format(windows_len))

    for window in range(windows_len):
        window_list = list()
        remaining_window_time = constants.WINDOW_DURATION
        if not jobs_sorted:
            break
        for job in jobs_sorted:
            if job['duration'] > remaining_window_time:
                current_window_limit = window_info['begin_ts'] + constants.WINDOW_DURATION * (window + 1)
                if job['timestamp'] < current_window_limit:
                    logger.debug('Two conflitant jobs. Check your input')
                    return list()
                logger.debug('Window is full. Jumping to the next one')
                break
            window_list.append(job['id'])
            remaining_window_time -= job['duration']
            logger.debug('Job {0} added to the window. Remaining window time {1}'
                    .format(job['id'], remaining_window_time))
        jobs_sorted = [job for job in jobs_sorted if job['id'] not in window_list]
        logger.debug('Jobs list updated: {0}'.format(jobs_sorted))
        if window_list:
            jobid_array.append(window_list)
    return jobid_array
