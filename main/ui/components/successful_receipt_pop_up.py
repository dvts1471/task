from core.ui.components import BaseComponent
from core.ui.elements import BaseElement
from core.ui.elements.button import Button


class SuccessfulReceiptPopUp(BaseComponent):
    locator = '//*[@class="modalBody"]'

    title_text = BaseElement(locator=f"{locator}//h2")

    close_button = Button(locator=f'{locator}//button[@id="modal-success-close"]')

    def __init__(self) -> None:
        super().__init__(locator=self.locator)
