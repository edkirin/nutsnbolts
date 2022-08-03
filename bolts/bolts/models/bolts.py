from typing import Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from bolts.database import Base


class BoltsModel(Base):
    __tablename__ = "bolts"

    id = Column(Integer, primary_key=True, index=True)
    counter = Column(Integer)

    @classmethod
    def get_last_counter(cls, db: Session) -> Optional["BoltsModel"]:
        return db.query(BoltsModel).order_by(BoltsModel.id.desc()).first()

    @classmethod
    def add_counter(cls, db: Session, counter: int):
        model = BoltsModel(
            counter=counter,
        )
        db.add(model)
        db.commit()
