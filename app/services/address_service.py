from sqlalchemy.orm import Session
from app.models.address_model import Address
from app.schemas.address_schema import AddressCreate


def create_address(db: Session, address: AddressCreate):

    new_address = Address(**address.dict())

    db.add(new_address)
    db.commit()
    db.refresh(new_address)

    return new_address


def update_address(db: Session, address_id: int, address_data: AddressCreate):

    address = db.query(Address).filter(Address.id == address_id).first()

    if not address:
        return None

    for key, value in address_data.dict().items():
        setattr(address, key, value)

    db.commit()
    db.refresh(address)

    return address


def delete_address(db: Session, address_id: int):

    address = db.query(Address).filter(Address.id == address_id).first()

    if not address:
        return False

    db.delete(address)
    db.commit()

    return True