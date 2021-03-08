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
                "vehicles": [],
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
            f"dealers/2", data=json.dumps({"phone": "323-372-2514"})
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
        assert resp.json() == []
