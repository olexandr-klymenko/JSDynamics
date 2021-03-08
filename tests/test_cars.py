from tests.base import TestApiBase


class TestCarsApi(TestApiBase):
    def test_get_all_dealers(self):
        resp = self.get("dealers", params={"email": "info@fast_deal.com"})
        assert resp.status_code == 200
        assert resp.json() == []
