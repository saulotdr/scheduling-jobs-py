import logging
from sys import stdout
from os import environ as env

''' Constants '''
JSON_HEADER = {'Content-Type': 'application/json'}
WINDOW_BEGIN = 'JANELA_INICIO'
WINDOW_END = 'JANELA_FIM'

''' Environment variables '''
PRETTY_PRINT = env['PRETTY_PRINT'] if 'PRETTY_PRINT' in env else False
LOGGING_LEVEL = env['LOG_LVL'] if 'LOG_LVL' in env else logging.ERROR

''' Logging configuration '''
logging.basicConfig(level=LOGGING_LEVEL,
                    stream=stdout,
                    format='%(asctime)s [%(levelname)s] - %(funcName)s: %(message)s')
