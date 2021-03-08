import json

from tests.base import TestApiBase


class TestCarsApi(TestApiBase):
    def test_get_dealers(self):
        resp = self.get("dealers", params={"email": "info@fast_deal.com"})
        assert resp.status_code == 200
        assert resp.json() == [
            {
                "location": "Houston Texas",
                "email": "info@fast_deal.com",
                "phone": "832-555-2002",
                "website": "fast_deal.com",
                "vehicles": [
                    {
                        "vin": "JH4KA8160PC000949",
                        "make": "Acura",
                        "model": "Legend",
                        "year": 1993,
                        "trim": "DX",
                        "id": "1",
                        "dealer_id": 1,
                    },
                    {
                        "vin": "2GCHG31K6J4141689",
                        "make": "Chevrolet",
                        "model": "G30",
                        "year": 1988,
                        "trim": "LX",
                        "id": "2",
                        "dealer_id": 1,
                    },
                    {
                        "vin": "ZAMGJ45A480037578",
                        "make": "Maserati",
                        "model": "GranTurismo",
                        "year": 2008,
                        "trim": "DX",
                        "id": "3",
                        "dealer_id": 1,
                    },
                ],
                "id": 1,
            }
        ]

    def test_create_and_delete_dealer(self):
        create_resp = self.post(
            "dealers",
            data=json.dumps(
                {
                    "location": "Somewhere",
                    "email": "info@some_email.com",
                    "phone": "111-111-1111",
                    "website": "some_email.com",
                }
            ),
        )
        assert create_resp.status_code == 201
        assert create_resp.json()["email"] == "info@some_email.com"

        dealer_id = create_resp.json()["id"]

        delete_resp = self.delete(f"dealers/{dealer_id}")
        assert delete_resp.status_code == 204

        get_resp = self.get("dealers", params={"email": "info@some_email.com"})
        assert get_resp.json() == []

    def test_update_dealer(self):
        update_resp = self.patch(
            "dealers/2", data=json.dumps({"phone": "323-372-2514"})
        )
        assert update_resp.status_code == 200
        assert update_resp.json() == {
            "location": "Los Angeles CA",
            "email": "info@best_cars.com",
            "phone": "323-372-2514",
            "website": "best_cars.com",
            "vehicles": [],
            "id": 2,
        }

    def test_get_all_vehicles_at_a_dealer(self):
        resp = self.get("dealers/1/vehicles")
        assert resp.status_code == 200
        assert resp.json() == [
            {
                "vin": "JH4KA8160PC000949",
                "make": "Acura",
                "model": "Legend",
                "year": 1993,
                "trim": "DX",
                "id": "1",
                "dealer_id": 1,
            },
            {
                "vin": "2GCHG31K6J4141689",
                "make": "Chevrolet",
                "model": "G30",
                "year": 1988,
                "trim": "LX",
                "id": "2",
                "dealer_id": 1,
            },
            {
                "vin": "ZAMGJ45A480037578",
                "make": "Maserati",
                "model": "GranTurismo",
                "year": 2008,
                "trim": "DX",
                "id": "3",
                "dealer_id": 1,
            },
        ]

    def test_create_vehicle(self):
        create_resp = self.post(
            "dealers/2/vehicles",
            data=json.dumps(
                {
                    "vin": "1FVABPAL91HH92692",
                    "make": "Freightliner",
                    "model": "Medium Conventional",
                    "year": 2001,
                    "trim": "LS",
                }
            ),
        )
        assert create_resp.status_code == 201
        assert create_resp.json()["vin"] == "1FVABPAL91HH92692"

    def test_update_vehicle(self):
        get_resp = self.get("dealers/3/vehicles")
        assert get_resp.status_code == 200
        vehicle_id = get_resp.json()[0]["id"]

        update_resp = self.patch(
            f"vehicles/{vehicle_id}", data=json.dumps({"trim": "GL"})
        )
        assert update_resp.status_code == 200
        assert update_resp.json()["trim"] == "GL"

    def test_delete_vehicle(self):
        get_resp = self.get("dealers/4/vehicles")
        assert get_resp.status_code == 200
        vehicle_id = get_resp.json()[0]["id"]

        delete_resp = self.delete(f"vehicles/{vehicle_id}")
        assert delete_resp.status_code == 204

        get_resp = self.get("dealers/4/vehicles")
        assert get_resp.status_code == 200
        assert get_resp.json() == []
