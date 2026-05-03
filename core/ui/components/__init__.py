from abc import ABC
from typing import Any

from core.ui.elements import BaseElement
from core.utils.driver_manager import DriverManager
from core.utils.logger import Logger


class BaseComponent(ABC, BaseElement):

    def __init__(self, locator: str) -> None:
        super().__init__(locator=locator)
        self.logger = Logger(self.__class__.__name__)

    @property
    def driver(self) -> Any:
        return DriverManager().driver