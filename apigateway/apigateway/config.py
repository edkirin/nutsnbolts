import os
from typing import List
from dataclasses import dataclass


@dataclass
class ServiceConfig:
    host: str
    name: str


class Config:
    nuts_host: str = os.environ.get('NUTS_HOST')
    bolts_host: str = os.environ.get('BOLTS_HOST')
    services: List[ServiceConfig] = [
        ServiceConfig(
            name="Nuts",
            host=nuts_host,
        ),
        ServiceConfig(
            name="Bolts",
            host=bolts_host,
        ),
    ]
