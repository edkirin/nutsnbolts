from fastapi import FastAPI
from bolts.database import engine, Base
from bolts.routers import ping
from bolts.routers import counter


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(ping.router)
app.include_router(counter.router)
