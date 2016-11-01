# flatten

[![Build Status](https://travis-ci.org/jaythomas/flatten-example-python.svg?branch=master)](https://travis-ci.org/jaythomas/flatten-example-python)

Example of how to flatten a list without using the built-in `.flatten()`.

## Linting and Testing

Build and run commands from the docker container:

```bash
docker build -t test .
docker run test pylint flatten.py
docker run test python flatten.test.py
```
