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
