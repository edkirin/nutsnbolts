from fastapi import FastAPI
from apigateway.routers import ping
from apigateway.routers import nuts
from apigateway.routers import bolts

app = FastAPI()
app.include_router(ping.router)
app.include_router(nuts.router)
app.include_router(bolts.router)
