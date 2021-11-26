# Lawfully

[![build](https://github.com/meyer1994/lawfully/actions/workflows/build.yml/badge.svg)](https://github.com/meyer1994/lawfully/actions/workflows/build.yml)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Declarative interface to test HTTP endpoints

## Table of Contents

- [About](#about)
- [Install](#install)
- [Usage](#usage)

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

It works with python's `unittest` module:

```py
# test.py
from lawfully import contract

@contract
class Test:
    """ My cool test """
    pass
```

```sh
$ python -m unittest -vb test.py
test (test.Test)
My cool test ... ok

----------------------------------------------------------------------
Ran 1 test in 0.010s

OK
```

[1]: https://pydantic-docs.helpmanual.io/
[2]: https://www.python-httpx.org/
