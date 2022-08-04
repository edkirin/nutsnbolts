from fastapi import APIRouter, Request
from apigateway.config import Config
from apigateway.proxy import Proxy


router = APIRouter()


@router.get("/bolts/{path:path}")
async def bolts_proxy(request: Request, path: str):
    proxy = Proxy(
        method=request.method,
        request=request,
        host=Config.bolts_host,
        path=f"/bolts/{path}",
    )

    return await proxy.execute()
