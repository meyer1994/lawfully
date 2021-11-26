from functools import wraps
from unittest import TestCase

import httpx
from pydantic import BaseModel


class Base:
    url = ''
    method = 'GET'
    base_url = 'http://localhost:8000'

    class Request:
        Body = BaseModel
        Params = BaseModel
        Headers = BaseModel

    class Response:
        Body = BaseModel
        Headers = BaseModel

    def setUp(self):
        self.client = httpx.Client(base_url=self.base_url)

    def request(self, *args, **kwargs):
        return self.client.request(self.method, self.url, *args, **kwargs)

    def test(self):
        body = dict(self.Request.Body())
        params = dict(self.Request.Params())
        headers = dict(self.Request.Headers())

        res = self.request(json=body, params=params, headers=headers)

        self.Response.Body(**res.json())
        self.Response.Headers(**res.headers)


def contract(cls):

    @wraps(cls, updated=())
    class T(cls, Base, TestCase):

        if hasattr(cls, 'Request'):
            class Request(cls.Request, Base.Request):
                pass

        if hasattr(cls, 'Response'):
            class Response(cls.Response, Base.Response):
                pass

    T.test.__doc__ = cls.__doc__

    return T
