from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from nuts.schemas.response import CounterSchema
from nuts.dependencies import get_db
from nuts.models import NutsModel


router = APIRouter()


@router.get("/counter", response_model=CounterSchema)
async def ping(db: Session = Depends(get_db)):
    model = NutsModel.get_last_counter(db)
    counter = model.counter if model is not None else 0
    NutsModel.add_counter(db, counter=counter + 1)

    response = CounterSchema(
        value=counter,
        message=f"Counter value is now {counter}"
    )
    return response
