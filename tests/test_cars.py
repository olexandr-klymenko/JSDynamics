from tests.base import TestApiBase


class TestCarsApi(TestApiBase):
    def test_get_all_dealers(self):
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
