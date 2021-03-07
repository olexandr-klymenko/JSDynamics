from datetime import date
from typing import List, Optional

from pydantic import BaseModel
from pydantic.fields import Field

VIN_LENGTH = 17


class VehicleBase(BaseModel):
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


class VehicleCreate(VehicleBase):
    pass


class Vehicle(VehicleBase):
    id: str

    class Config:
        orm_mode = True


class DealerBase(BaseModel):
    name: str
    location: str
    email: str
    phone: str
    website: str


class DealerCreate(DealerBase):
    pass


class DealerUpdate(DealerBase):
    name: Optional[str]
    location: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    website: Optional[str]


class Dealer(DealerBase):
    id: int

    vehicles: List[Vehicle] = []

    class Config:
        orm_mode = True
