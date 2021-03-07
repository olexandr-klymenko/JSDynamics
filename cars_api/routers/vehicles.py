from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from cars_api import crud, schemas
from cars_api.database import get_db

router = APIRouter()

VehicleNotFound = HTTPException(status_code=404, detail="Vehicle not found")


@router.get("/{vehicle_id}", response_model=schemas.Vehicle)
def read_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    db_vehicle = crud.get_vehicle(db, vehicle_id=vehicle_id)
    if db_vehicle is None:
        raise VehicleNotFound
    return db_vehicle


@router.patch("/{vehicle_id}", response_model=schemas.Vehicle)
def update_vehicle(
    vehicle_id: int, vehicle: schemas.VehicleUpdate, db: Session = Depends(get_db)
):
    db_vehicle = crud.get_vehicle(db, vehicle_id=vehicle_id)
    if db_vehicle is None:
        raise VehicleNotFound

    return crud.update_vehicle(
        db=db, db_vehicle=db_vehicle, data=vehicle.dict(exclude_unset=True)
    )


@router.delete("/{vehicle_id}", status_code=204)
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    db_vehicle = crud.get_vehicle(db, vehicle_id=vehicle_id)
    if db_vehicle is None:
        raise VehicleNotFound

    crud.delete_vehicle(db, db_vehicle=db_vehicle)


@router.get("/", response_model=List[schemas.Vehicle])
def read_vehicles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_vehicles(db, skip=skip, limit=limit)
