from core.ui.components import BaseComponent
from core.ui.elements.button import Button
from core.ui.elements.input import Input


class BetSlip(BaseComponent):
    locator = '//*[@class="betSlip"]'

    stake_input = Input(locator=f'{locator}//*[@id="bet-slip-stake-input"]')
    place_bet_button = Button(locator=f'{locator}//*[@id="bet-slip-place-bet"]')


    def __init__(self) -> None:
        super().__init__(locator=self.locator)





