from fastapi import APIRouter
from nuts.schemas.response import PingSchema


router = APIRouter()


@router.get("/ping", response_model=PingSchema)
async def ping():
    response = PingSchema(
        result="PONG from nuts service!"
    )
    return response
