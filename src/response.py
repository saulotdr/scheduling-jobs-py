import constants
from flask import jsonify
from http import HTTPStatus


def ok(response_array):
    return jsonify(response_array), HTTPStatus.OK, constants.JSON_HEADER


def error():
    return jsonify([]), HTTPStatus.BAD_REQUEST, constants.JSON_HEADER
