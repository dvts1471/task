from abc import ABC
from typing import Any

import allure

from config import APP_URL
from core.utils.driver_manager import DriverManager
from core.utils.logger import Logger


class BasePage(ABC):
    url: str | None = APP_URL

    def __init__(self) -> None:
        self.logger = Logger(self.__class__.__name__)

    @property
    def driver(self) -> Any:
        return DriverManager().driver

    def open(self) -> 'BasePage':
        with allure.step(f"Open {self.__class__.__name__}"):
            self.logger.info(f"Open {self.__class__.__name__}")
            self.driver.get(url=self.url)
            return self

    def wait_loaded(self, timeout: int = 5) -> 'BasePage':
        return self

    def is_loaded(self, timeout: int = 5) -> bool:
        raise NotImplementedError