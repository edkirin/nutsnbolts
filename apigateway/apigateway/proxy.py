from fastapi import Request, Response
import httpx
from urllib.parse import urljoin
from typing import Optional


class Proxy:
    def __init__(self, method: str, request: Request, host: str, path: str):
        self.method = method.lower()
        self.request = request
        self.host = host
        self.path = path

    async def execute(self, method: Optional[str] = None, **kwargs) -> Response:
        headers = dict(self.request.headers.items())
        headers["x-source"] = "public"

        params = {
            "url": urljoin(self.host, self.path),
            "headers": headers,
        }

        if "content-length" in headers:
            del headers["content-length"]
            body = await self.request.body()
            if body:
                params["content"] = body

        async with httpx.AsyncClient() as client:
            method = getattr(client, method if method is not None else self.method)
            proxy = await method(**params)

        response = Response()
        response.body = proxy.content
        response.status_code = proxy.status_code
        response.headers["content-type"] = proxy.headers["content-type"]
        response.headers["content-length"] = str(len(proxy.content))

        return response

    async def post(self, **kwargs) -> Response:
        return await self.execute("post", **kwargs)
