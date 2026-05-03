from typing import Any

import allure
from requests import Response
from core.api.api_client import ApiClient


class BalanceClient(ApiClient):
    SERVICE = ""

    @allure.step("Reset balance")
    def reset_balance(self, **kwargs: Any) -> Response:
        url = self.service_url
        response = self.send_request(
            method="POST", url=f"{url}/reset-balance", body=kwargs
        )
        return response

    @allure.step("Get balance")
    def get_balance(self, **kwargs: Any) -> Response:
        url = self.service_url
        response = self.send_request(method="GET", url=f"{url}/balance", body=kwargs)
        return response
