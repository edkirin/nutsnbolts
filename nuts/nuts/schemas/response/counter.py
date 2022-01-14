from pydantic import BaseModel


class CounterSchema(BaseModel):
    message: str
    value: int
