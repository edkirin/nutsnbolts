from typing import Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from nuts.database import Base


class NutsModel(Base):
    __tablename__ = "nuts"

    id = Column(Integer, primary_key=True, index=True)
    counter = Column(String)

    @classmethod
    def get_last_counter(cls, db: Session) -> Optional["NutsModel"]:
        return (
            db.
            query(NutsModel).
            order_by(NutsModel.id.desc()).
            first()
        )

    @classmethod
    def add_counter(cls, db: Session, counter: int):
        model = NutsModel(
            counter=counter,
        )
        db.add(model)
        db.commit()
