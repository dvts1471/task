import allure
import pytest
from typing import Generator

from core.utils.driver_manager import DriverManager
from main.api_clients.balance.balance_client import BalanceClient


@pytest.fixture
@allure.title("Reset user balance")
def reset_balance() -> None:
    balance_client = BalanceClient()
    response = balance_client.reset_balance()
    assert response.status_code == 200


@pytest.fixture
def driver() -> Generator[None, None, None]:
    yield
    if DriverManager.is_driver_initiated():
        DriverManager.close_driver()
