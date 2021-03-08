from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from cars_api import crud, schemas
from cars_api.database import get_db

router = APIRouter()

DealerNotFound = HTTPException(status_code=404, detail="Dealer not found")


@router.post("/", response_model=schemas.Dealer, status_code=201)
def create_dealer(dealer: schemas.DealerCreate, db: Session = Depends(get_db)):
    db_dealer = crud.get_dealer_by_email(db, email=dealer.email)
    if db_dealer:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_dealer(db=db, dealer=dealer)


@router.get("/{dealer_id}", response_model=schemas.Dealer)
def read_dealer(dealer_id: int, db: Session = Depends(get_db)):
    db_dealer = crud.get_dealer(db, dealer_id=dealer_id)
    if db_dealer is None:
        raise DealerNotFound
    return db_dealer


@router.patch("/{dealer_id}", response_model=schemas.Dealer)
def update_dealer(
    dealer_id: int, dealer: schemas.DealerUpdate, db: Session = Depends(get_db)
):
    db_dealer = crud.get_dealer(db, dealer_id=dealer_id)
    if db_dealer is None:
        raise DealerNotFound

    return crud.update_dealer(
        db=db, db_dealer=db_dealer, data=dealer.dict(exclude_unset=True)
    )


@router.delete("/{dealer_id}", status_code=204)
def delete_dealer(dealer_id: int, db: Session = Depends(get_db)):
    db_dealer = crud.get_dealer(db, dealer_id=dealer_id)
    if db_dealer is None:
        raise DealerNotFound

    crud.delete_dealer(db=db, db_dealer=db_dealer)


@router.get("/", response_model=List[schemas.Dealer])
def read_dealers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dealers = crud.get_dealers(db, skip=skip, limit=limit)
    return dealers


@router.post("/{dealer_id}/vehicles/", response_model=schemas.Vehicle)
def create_vehicle_for_dealer(
    dealer_id: int, vehicle: schemas.VehicleCreate, db: Session = Depends(get_db)
):
    return crud.create_vehicle(db=db, vehicle=vehicle, dealer_id=dealer_id)


@router.get("/{dealer_id}/vehicles/", response_model=List[schemas.Vehicle])
def get_vehicles_at_a_dealer(dealer_id: int, db: Session = Depends(get_db)):
    return crud.get_vehicles_at_a_dealer(db=db, dealer_id=dealer_id)
