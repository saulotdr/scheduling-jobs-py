import pytest
import json

from http import HTTPStatus
from src.constants import POST_ROUTE, WINDOW_BEGIN_KEY, WINDOW_END_KEY


def test_process_jobs_array_invalid(client, invalid_input_data):
    data_file = open('res/jobs_invalid.json').read()
    data = json.loads(data_file)
    response = client.post(POST_ROUTE, 
            json=data,
            headers={
              WINDOW_BEGIN_KEY : "2019-11-10 09:00:00",
              WINDOW_END_KEY : "2019-11-11 12:00:00"
            })
    
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert type(response.get_json()) is list
    assert response.get_json() == invalid_input_data


def test_process_jobs_array_dataset1(client, expected_body_dataset1):
    data_file = open('res/jobs_datasets1.json').read()
    data = json.loads(data_file)
    response = client.post(POST_ROUTE, 
            json=data,
            headers={
              WINDOW_BEGIN_KEY : "2019-11-10 09:00:00",
              WINDOW_END_KEY : "2019-11-11 12:00:00"
            })

    response_body = response.get_json()

    assert response.status_code == HTTPStatus.OK
    assert type(response_body) is list
    assert response_body == expected_body_dataset1

def test_process_jobs_array_dataset2(client, expected_body_dataset2):
    data_file = open('res/jobs_datasets2.json').read()
    data = json.loads(data_file)
    response = client.post(POST_ROUTE, 
            json=data,
            headers={
              WINDOW_BEGIN_KEY : "2019-11-10 09:00:00",
              WINDOW_END_KEY : "2019-11-11 12:00:00"
            })

    response_body = response.get_json()

    assert response.status_code == HTTPStatus.OK
    assert type(response_body) is list
    assert response_body == expected_body_dataset2

    import pytest

def test_process_jobs_array_conflitant(client, expected_body_conflitant_dataset):
    data_file = open('res/jobs_conflitant.json').read()
    data = json.loads(data_file)
    response = client.post(POST_ROUTE, 
            json=data,
            headers={
              WINDOW_BEGIN_KEY : "2019-11-10 09:00:00",
              WINDOW_END_KEY : "2019-11-10 18:00:00"
            })

    response_body = response.get_json()

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert type(response_body) is list
    assert response_body == expected_body_conflitant_dataset
