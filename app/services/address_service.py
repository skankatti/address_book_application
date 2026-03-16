from sqlalchemy.orm import Session
from app.models.address_model import Address


def create_address(db: Session, address):

    new_address = Address(**address.dict())

    db.add(new_address)
    db.commit()
    db.refresh(new_address)

    return new_address