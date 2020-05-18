import os
import tempfile
import pytest
from src.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client


@pytest.fixture
def expected_body_dataset1():
    body = [
        [1, 3],
        [2]
    ]
    return body


@pytest.fixture
def expected_body_dataset2():
    body = [
        [4, 1],
        [3], 
        [2]
    ]
    return body

@pytest.fixture
def expected_body_conflitant_dataset():
    return []

@pytest.fixture
def invalid_input_data():
    return []
