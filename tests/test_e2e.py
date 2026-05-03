
import allure
import pytest

from main.api_clients.balance.balance_client import BalanceClient
from main.ui.pages.dashboard_page import DashboardPage
from core.utils import verify


class TestE2E:
    @pytest.mark.ui
    @pytest.mark.e2e
    @pytest.mark.critical
    @allure.title("Test successful bet placement")
    @allure.description("This test verifies that user can place bet successfully and balance is updated accordingly")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('e2e')
    def test_successful_bet_placement(self, driver: None, reset_balance: None) -> None:
        balance_client = BalanceClient()
        balance_before = balance_client.get_balance().json()['balance']

        dashboard_page = DashboardPage().open().wait_loaded()

        with allure.step("Click on any Odd button for any match in the Match List"):
            test_match = dashboard_page.match_list.get_matches()[0]
            test_match.home_odds_button.click()

        with allure.step('Fill positive number (in range 1<=x<=100) to "Stake" input field'):
            stake = 10
            dashboard_page.bet_slip.stake_input.fill(str(stake))

        with allure.step('Click on "Place Bet" button'):
            dashboard_page.bet_slip.place_bet_button.click()
            button_text = dashboard_page.bet_slip.place_bet_button.get_text()

            verify(
                check=button_text == "PLACING...",
                p_msg='Button text changed to "Placing..."',
                f_msg=f'Button text should be "Placing...". Actual: {button_text}'
            )

        with allure.step('Close "Bet Placed Successfully" confirmation'):
            dashboard_page.successful_receipt_pop_up.wait_element()
            dashboard_page.successful_receipt_pop_up.close_button.click()

            balance_after = balance_client.get_balance().json()['balance']

        with allure.step('Verify that balance has been decreased by the amount of stake'):
            verify(
                check=balance_after == balance_before - stake,
                p_msg=f"Balance decreased by {stake}",
                f_msg=f"Balance should be decreased by {stake}. Actual: {balance_after}"
            )


