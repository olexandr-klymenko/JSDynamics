from cars_api.database import SessionLocal
from cars_api import crud, schemas
from scripts.init_db import init_db


TEST_DEALERS = [
    {
        "location": "Houston Texas",
        "email": "info@fast_deal.com",
        "phone": "832-555-2002",
        "website": "fast_deal.com",
        "id": 1,
    },
    {
        "location": "Los Angeles CA",
        "email": "info@best_cars.com",
        "phone": "323-372-2515",
        "website": "best_cars.com",
        "id": 2,
    },
    {
        "location": "Chicago, IL",
        "email": "info@cheap_cars.com",
        "phone": "217-300-2642",
        "website": "cheap_cars.com",
        "id": 3,
    },
    {
        "location": "New York, NY",
        "email": "info@cool_cars.com",
        "phone": "212-200-1266",
        "website": "cool_cars.com",
        "id": 4,
    },
]


TEST_VEHICLES = {}


def init_test_data():
    db = SessionLocal()
    for dealer_data in TEST_DEALERS:
        dealer = schemas.DealerCreate(**dealer_data)
        crud.create_dealer(db=db, dealer=dealer)


if __name__ == "__main__":
    init_db()
    init_test_data()
