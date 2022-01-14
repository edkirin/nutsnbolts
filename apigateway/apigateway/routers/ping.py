from fastapi import APIRouter
import httpx
import asyncio
from time import perf_counter
from urllib.parse import urljoin
from apigateway.schemas.response import PingSchema, ServiceSchema
from apigateway.config import Config, ServiceConfig


router = APIRouter()


@router.get("/ping", response_model=PingSchema)
async def ping():

    async def ping_service(client: httpx.AsyncClient, service: ServiceConfig, response: PingSchema):
        try:
            ping_time = perf_counter()
            resp = await client.get(
                url=urljoin(service.host, 'ping'),
                headers={
                    'x-source': 'internal',
                },
            )
            ping_time = perf_counter() - ping_time
            response.services.append(
                ServiceSchema(
                    name=service.name,
                    host=service.host,
                    health="OK" if resp.status_code == 200 else "Not OK",
                    status_code=resp.status_code,
                    ping_time=f'{ping_time:0.4f}',
                )
            )
        except Exception:
            response.services.append(
                ServiceSchema(
                    name=service.name,
                    host=service.host,
                    health="Not available",
                )
            )

    response = PingSchema(
        services=list()
    )

    async with httpx.AsyncClient() as client:
        await asyncio.gather(*[ping_service(client, service, response) for service in Config.services])

    return response
