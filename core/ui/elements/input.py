import allure

from core.ui.elements import BaseElement


class Input(BaseElement):
    def fill(self, text: str) -> None:
        with allure.step(f'Fill {self.__class__.__name__}({self.locator}) with "{text}"'):
            self.logger.debug(f'Fill {self.__class__.__name__}({self.locator}) "{text}"')
            self.element.send_keys(text)

    def clear(self) -> None:
        with allure.step(f'Clear {self.__class__.__name__}({self.locator})'):
            self.logger.debug(f"Clear {self.__class__.__name__}({self.locator})")
            self.element.clear()