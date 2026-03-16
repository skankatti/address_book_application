from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.address_schema import AddressCreate, AddressResponse
from app.services.address_service import create_address, update_address, delete_address


router = APIRouter(
    prefix="/addresses",
    tags=["Addresses"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AddressResponse)
def create(addr: AddressCreate, db: Session = Depends(get_db)):
    return create_address(db, addr)


@router.put("/{address_id}", response_model=AddressResponse)
def update(address_id: int, addr: AddressCreate, db: Session = Depends(get_db)):

    address = update_address(db, address_id, addr)

    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    return address


@router.delete("/{address_id}")
def delete(address_id: int, db: Session = Depends(get_db)):

    success = delete_address(db, address_id)

    if not success:
        raise HTTPException(status_code=404, detail="Address not found")

    return {"message": "Address deleted"}