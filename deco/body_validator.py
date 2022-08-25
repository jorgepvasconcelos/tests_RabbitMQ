import json
from functools import wraps
from typing import Type

from pydantic import BaseModel, ValidationError


class RequestExpected(BaseModel):
    value: int


def validate_body(body_schema: Type[BaseModel]):
    def validate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                decoded_body = args[3].decode('utf-8')
                body_schema(**json.loads(decoded_body))
                return fn(*args, **kwargs)

            except ValidationError as e:
                response = 'deu ruim'
                print(response)
                return response

        return wrapper

    return validate


def validate_body2(body_schema: Type[BaseModel]):
    def validate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                args_list = list(args)
                decoded_body = args_list[3].decode('utf-8')
                args_list[3] = body_schema(**json.loads(decoded_body))
                return fn(*args_list, **kwargs)

            except ValidationError as e:
                response = 'deu ruim'
                print(response)
                return response

        return wrapper

    return validate
