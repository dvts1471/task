from typing import Any

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from core.utils.driver_manager import DriverManager

from selenium.webdriver.support import expected_conditions as EC

from core.utils.logger import Logger


class BaseElement:
    logger = Logger(__name__)

    def __init__(self, locator: str) -> None:
        self.locator = locator

    def get_text(self) -> str:
        return self.element.text

    @property
    def driver(self) -> Any:
        return DriverManager().driver

    @property
    def element(self) -> WebElement:
        return self.wait_element()

    def wait_element(self, timeout: int = 5) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, self.locator))
        )

    def is_loaded(self, timeout: int = 5) -> bool:
        try:
            self.wait_element(timeout=timeout)
            return True
        except Exception:
            return False

    def click(self) -> None:
        with allure.step(f"Click on {self.__class__.__name__}({self.locator})"):
            self.logger.debug(f"Click on {self.__class__.__name__}({self.locator})")
            self.wait_element().click()
