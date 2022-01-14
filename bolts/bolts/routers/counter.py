from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from bolts.schemas.response import CounterSchema
from bolts.dependencies import get_db
from bolts.models import BoltsModel


router = APIRouter()


@router.get("/counter", response_model=CounterSchema)
async def ping(db: Session = Depends(get_db)):
    model = BoltsModel.get_last_counter(db)
    counter = model.counter if model is not None else 0
    BoltsModel.add_counter(db, counter=counter + 3)

    response = CounterSchema(
        value=counter,
        message=f"Counter value is now {counter}"
    )
    return response
