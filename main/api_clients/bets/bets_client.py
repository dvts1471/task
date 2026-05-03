from typing import Any

import allure
from requests import Response
from core.api.api_client import ApiClient


class BetsClient(ApiClient):
    SERVICE = ""

    @allure.step("Place bet")
    def place_bet(
        self, match_id: str, selection: str, stake: float, **kwargs: Any
    ) -> Response:
        url = f"{self.service_url}/place-bet"
        body = {"matchId": match_id, "selection": selection, "stake": stake, **kwargs}
        response = self.send_request(method="POST", url=url, body=body)

        return response
