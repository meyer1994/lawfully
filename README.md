# Lawfully

[![build](https://github.com/meyer1994/lawfully/actions/workflows/build.yml/badge.svg)](https://github.com/meyer1994/lawfully/actions/workflows/build.yml)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Declarative interface to test HTTP endpoints

## Table of Contents

- [About](#about)
- [Install](#install)
- [Usage](#usage)
- [Advanced](#advanced)

## About

I've created this because I was tired of writing boilerplate code to test HTTP
request which always did the same thing:

1. Write request
1. Perform request
1. Validate response

## Install

This module make use of [pydantic][1] for data validation and [httpx][2] for
HTTP requests.

```sh
$ pip install -r requirements.txt
```

## Usage

It works with python's `unittest` module. The [`example.py`](./example.py) file
shows a very simple way of using it.

```py
import uuid
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def get(page: int, size: int):
    return {
        'page': page,
        'size': size,
        'uuid': uuid.uuid4()
    }

from lawfully import contract
from pydantic import BaseModel

@contract
class Test:
    """ Tests the GET request """

    class Request:
        class Params(BaseModel):
            page: int = 5
            size: int = 10

    class Response:
        class Body(BaseModel):
            page: int
            size: int
            uuid: uuid.UUID
```

To run the example, first start the server, you can use [uvicorn][3]. Inside a
terminal:

```sh
$ uvicorn example:app
```

And then, just use python's `unittest` module to run the test:

```sh
$ python -m unittest -vb example.py
test (example.Test)
Tests the GET request ... ok

----------------------------------------------------------------------
Ran 1 test in 0.018s

OK
```

As easy as that.

## Advanced

This library was created with `pydantic` use in mind. However, it is not a
requirement. The only thing expected from the objects declared inside `Request`
and `Response` are that they return values that can be passed to `httpx`. For
example: `Body`, `Params` and `Headers` are expected to return a `dict` when
called. This way, something like this is totally acceptable:

```py
class Request:
    Params = lambda: {'page': 1}
```

Another thing that might be useful is that the class returned by the `@contract`
annotation is a `unittest.TestCase` class. This way, you can treat it like so.
Create another test method, custom `setUp` and `tearDown`, etc. The only
requirement is that you call the super class `setUp` method when overriding it.

```py
@contract
class Test:
    def setUp(self):
        super().setUp()
        # your code
```

[1]: https://pydantic-docs.helpmanual.io/
[2]: https://www.python-httpx.org/
[3]: https://www.uvicorn.org/
