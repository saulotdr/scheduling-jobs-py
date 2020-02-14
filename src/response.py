import constants
import logging
from flask import jsonify
from http import HTTPStatus

logger = logging.getLogger(__name__)


def ok(response_array):
    logger.debug(response_array)
    return jsonify(response_array), HTTPStatus.OK, constants.JSON_HEADER


def error():
    logger.debug([])
    return jsonify([]), HTTPStatus.BAD_REQUEST, constants.JSON_HEADER
