import os
import tempfile
import pytest

from src.app import process_jobs_array


@pytest.fixture
def client():
    app = process_jobs_array()
    return app
