import allure
import pytest

from core.api.api_expected_response import ApiExpectedResponse
from main.api_clients.bets.bets_client import BetsClient
from main.api_clients.bets.models import PlaceBetDto405
from main.api_clients.matches.matches_client import MatchesClient


class TestBets:
    @pytest.mark.api
    @pytest.mark.critical
    @allure.title("Test Put Bet over the users balance")
    @allure.description("This test attempts to place bet over the user budget")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("api")
    def test_put_bet_over_balance(self, reset_balance: None) -> None:
        matches_client = MatchesClient()
        bets_client = BetsClient()

        with allure.step("Define available match"):
            response = matches_client.get_all_matches()
            assert response.status_code == 200, response.json()
            all_matches = response.json()
            test_match = all_matches[0]

        with allure.step("Put bet to reduce user balance"):
            first_bet_response = bets_client.place_bet(
                match_id=test_match.get("id"), selection="HOME", stake=100
            )
            assert first_bet_response.status_code == 200, first_bet_response.json()

        with allure.step("Put bet with stake greater than users balance"):
            second_bet_response = bets_client.place_bet(
                match_id=test_match.get("id"), selection="HOME", stake=100
            )

            bets_client.verify_response(
                actual_response=second_bet_response,
                expected_response=ApiExpectedResponse(
                    status_code=405, model=PlaceBetDto405
                ),
            )
