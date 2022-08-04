from fastapi import APIRouter, Request
from apigateway.config import Config
from apigateway.proxy import Proxy


router = APIRouter()


@router.get("/nuts/{path:path}")
async def nuts_proxy(request: Request, path: str):
    proxy = Proxy(
        method=request.method,
        request=request,
        host=Config.nuts_host,
        path=f"/nuts/{path}",
    )

    return await proxy.execute()
