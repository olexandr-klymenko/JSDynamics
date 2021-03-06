import os
from typing import Any, Dict

import requests

DEFAULT_API_BASE_URL = "http://0.0.0.0:8000"


class TestApiBase:
    VALIDATION_ERROR = 422

    @property
    def api_base_url(self) -> str:
        return os.environ.get("API_BASE_URL", DEFAULT_API_BASE_URL)

    def post(self, url: str, data: str) -> requests.Response:
        return self._request("POST", f"{self.api_base_url}/{url}/", data=data)

    def get(self, url: str, params: Dict = None) -> requests.Response:
        return self._request("GET", f"{self.api_base_url}/{url}/", params=params)

    def delete(self, url: str) -> requests.Response:
        return self._request("DELETE", f"{self.api_base_url}/{url}/")

    def put(self, url: str, data: str, partial: bool = False) -> requests.Response:
        return self._request("PUT", f"{self.api_base_url}/{url}/", data=data)

    def patch(self, url: str, data: str) -> requests.Response:
        return self._request("PATCH", f"{self.api_base_url}/{url}/", data=data)

    @staticmethod
    def _request(
            method: str, url: str, params: Any = None, data: Any = None
    ) -> requests.Response:
        session = requests.Session()
        return session.request(method, url, params, data)
