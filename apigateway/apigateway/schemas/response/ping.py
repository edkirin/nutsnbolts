from typing import List, Optional
from pydantic import BaseModel


class ServiceSchema(BaseModel):
    name: str
    host: str
    health: str
    status_code: Optional[int]
    ping_time: Optional[str]


class PingSchema(BaseModel):
    services: List[ServiceSchema]
