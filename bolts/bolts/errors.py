from fastapi import HTTPException, status
from typing import Optional


class HTTPExceptionBase(HTTPException):
    status_code: Optional[int]

    def __init__(self, *args, **kwargs):
        kwargs['status_code'] = self.status_code
        super().__init__(*args, **kwargs)


class UnauthorizedError(HTTPExceptionBase):
    status_code = status.HTTP_401_UNAUTHORIZED


class NotFoundError(HTTPExceptionBase):
    status_code = status.HTTP_404_NOT_FOUND


class UnprocessableEntryError(HTTPExceptionBase):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
