from typing import List

from selenium.webdriver.common.by import By

from core.ui.components import BaseComponent
from core.ui.elements.button import Button


class Match(BaseComponent):
    locator_template = '//*[@class="card matchCard" and @id="{match_id}"]'

    def __init__(self, match_id: str) -> None:
        locator = self.locator_template.format(match_id=match_id)
        self.match_id = match_id
        super().__init__(locator=locator)
        self.home_odds_button = Button(locator='//button[contains(@id, "home")]')
        self.draw_odds_button = Button(locator='//button[contains(@id, "draw")]')
        self.away_odds_button = Button(locator='//button[contains(@id, "away")]')


class MatchList(BaseComponent):
    locator = '//*[@class="matchList"]'

    def __init__(self) -> None:
        super().__init__(locator=self.locator)

    def get_matches(self) -> List["Match"]:
        match_elements = self.driver.find_elements(
            By.XPATH, f'{self.locator}//*[@class="card matchCard"]'
        )
        matches: List[Match] = []
        for element in match_elements:
            match_id = element.get_attribute("id")
            matches.append(Match(match_id=match_id))
        return matches
