from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from cars_api import crud, models, schemas
from cars_api.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/dealers/", response_model=schemas.Dealer, status_code=201)
def create_dealer(dealer: schemas.DealerCreate, db: Session = Depends(get_db)):
    db_dealer = crud.get_dealer_by_email(db, email=dealer.email)
    if db_dealer:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_dealer(db=db, dealer=dealer)


@app.get("/dealers/{dealer_id}", response_model=schemas.Dealer)
def read_dealer(dealer_id: int, db: Session = Depends(get_db)):
    db_dealer = crud.get_dealer(db, dealer_id=dealer_id)
    if db_dealer is None:
        raise HTTPException(status_code=404, detail="Dealer not found")
    return db_dealer


@app.patch("/dealers/{dealer_id}", response_model=schemas.Dealer)
def update_dealer(
    dealer_id: int, dealer: schemas.DealerUpdate, db: Session = Depends(get_db)
):
    db_dealer = crud.get_dealer(db, dealer_id=dealer_id)
    if db_dealer is None:
        raise HTTPException(status_code=404, detail="Dealer not found")

    return crud.update_dealer(
        db=db, db_dealer=db_dealer, data=dealer.dict(exclude_unset=True)
    )


@app.delete("/dealers/{dealer_id}", status_code=204)
def delete_dealer(dealer_id: int, db: Session = Depends(get_db)):
    db_dealer = crud.get_dealer(db, dealer_id=dealer_id)
    if db_dealer is None:
        raise HTTPException(status_code=404, detail="Dealer not found")

    crud.delete_dealer(db=db, db_dealer=db_dealer)


@app.get("/dealers/", response_model=List[schemas.Dealer])
def read_dealers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dealers = crud.get_dealers(db, skip=skip, limit=limit)
    return dealers


@app.post("/dealers/{dealer_id}/vehicles/", response_model=schemas.Vehicle)
def create_vehicle_for_dealer(
    dealer_id: int, vehicle: schemas.VehicleCreate, db: Session = Depends(get_db)
):
    return crud.create_vehicle(db=db, vehicle=vehicle, dealer_id=dealer_id)


@app.get("/vehicles/", response_model=List[schemas.Vehicle])
def read_vehicles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_vehicles(db, skip=skip, limit=limit)


@app.delete("/vehicles/{vehicle_id}", status_code=204)
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    db_vehicle = crud.get_vehicle(db, vehicle_id=vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    crud.delete_vehicle(db, db_vehicle=db_vehicle)


@app.patch("/vehicles/{vehicle_id}", response_model=schemas.Vehicle)
def update_vehicle(
    vehicle_id: int, vehicle: schemas.VehicleUpdate, db: Session = Depends(get_db)
):
    db_vehicle = crud.get_vehicle(db, vehicle_id=vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    return crud.update_vehicle(
        db=db, db_vehicle=db_vehicle, data=vehicle.dict(exclude_unset=True)
    )
