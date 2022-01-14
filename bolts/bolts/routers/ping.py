from fastapi import APIRouter
from bolts.schemas.response import PingSchema


router = APIRouter()


@router.get("/ping", response_model=PingSchema)
async def ping():
    response = PingSchema(
        result="PONG from bolts service!"
    )
    return response
