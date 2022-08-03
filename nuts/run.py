from os import pread
from fastapi import FastAPI
from nuts.database import engine, Base
from nuts.routers import ping
from nuts.routers import counter


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(ping.router, prefix="/nuts")
app.include_router(counter.router, prefix="/nuts")
