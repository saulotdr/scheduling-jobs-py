import logging
from sys import stdout
from os import environ as env

''' Constants '''
JSON_HEADER = {'Content-Type': 'application/json'}
WINDOW_BEGIN_KEY = 'JANELA_INICIO'
WINDOW_END_KEY = 'JANELA_FIM'
WINDOW_DURATION = 28800  # 8 hours in ms
POST_ROUTE = '/api/jobs'

''' Environment variables '''
LOGGING_LEVEL = env['LOG_LVL'] if 'LOG_LVL' in env else logging.ERROR

''' Logging configuration '''
logging.basicConfig(level=LOGGING_LEVEL,
            stream=stdout,
            format='%(asctime)s [%(levelname)s] - %(funcName)s: %(message)s')
