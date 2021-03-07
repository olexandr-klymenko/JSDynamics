from tests.base import TestApiBase


class TestCarsApi(TestApiBase):
    def test_get_all_dealers(self):
        resp = self.get("dealers")
        assert resp.status_code == 200
        assert resp.json() == []
