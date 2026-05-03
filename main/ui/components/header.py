from core.ui.components import BaseComponent


class Header(BaseComponent):
    locator = "//header"

    def __init__(self) -> None:
        super().__init__(locator=self.locator)
