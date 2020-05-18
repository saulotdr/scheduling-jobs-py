import src.constants as constants

import logging
from flask import jsonify
from http import HTTPStatus

logger = logging.getLogger(__name__)


def ok(response_list):
    logger.debug(response_list)
    return jsonify(response_list), HTTPStatus.OK, constants.JSON_HEADER


def error():
    logger.debug([])
    return jsonify([]), HTTPStatus.BAD_REQUEST, constants.JSON_HEADER
