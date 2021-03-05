from datetime import date
from typing import List

from pydantic import BaseModel
from pydantic.fields import Field

VIN_LENGTH = 17


class Vehicle(BaseModel):
    id: str
    vin: str = Field(
        ...,
        min_length=VIN_LENGTH,
        max_length=VIN_LENGTH,
        title="Vehicle Identification Number",
    )
    make: str
    model: str
    year: date
    trim: str

    dealer_id: int

    class Config:
        orm_mode = True


class Dealer(BaseModel):
    id: str
    name: str
    location: str
    email: str
    phone: str
    website: str

    vehicles: List[Vehicle] = []

    class Config:
        orm_mode = True
