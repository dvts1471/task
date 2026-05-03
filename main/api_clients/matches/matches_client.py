import allure
from requests import Response
from core.api.api_client import ApiClient


class MatchesClient(ApiClient):
    SERVICE = "/matches"

    @allure.step("Get all matches")
    def get_all_matches(self) -> Response:
        url = self.service_url
        response = self.send_request(
            method='GET',
            url=url,
        )
        return response