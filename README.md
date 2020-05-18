# Scheduling jobs web service
🐍 [![Python version](https://img.shields.io/badge/python-3.8-green)](https://python.org)</br>
🌶 [![Flask version](https://img.shields.io/badge/flask-1.1.2-red)](https://python.org)

## Getting started 

This web server implements all the requirements needed by client. The requirements document is available [here](requirements.pdf)

This solution uses [Flask](https://github.com/pallets/flask) framework.

## Configuration

Environment variables to be configured (all are optional):

| Variable | Description | Default value | Accepted values |
| -------- | ----------- | ------------- | --------------- |
| LOG_LVL | Set the logging level across the module | ERROR | [Logging Levels](https://docs.python.org/3/library/logging.html#levels) |

## Dependencies

You should install [Pipenv](https://docs.pipenv.org), a package tool for Python that simplifies dependency management.

```bash
$ sudo pip3 install pipenv
```

After install pipenv, enter in the project's root folder and install all packages dependencies described in Pipfile

```bash
$ pipenv install
```

If you are developing using WSL environment, you should specify the python binary to pipenv command:

```bash
$ pipenv install --python=/usr/bin/python3.8
```

## Running the web server

In the project's root folder, run the flask app globally and with the desired port

```
$ pipenv shell
$ export FLASK_APP=src/route.py
$ flask run --host=0.0.0.0 --port=8080
```

## Tests

The unit tests can be executed in the section below:

- [integration tests](tests/integration)
