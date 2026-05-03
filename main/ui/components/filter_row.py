from core.ui.components import BaseComponent


class FilterRow(BaseComponent):
    locator = '//*[@class="filterRow"]'
    date_filter = BaseComponent(
        locator=f'{locator}//*[@id="date-filter"]'
    )  # ToDo: implement date filter component
    odds_filter = BaseComponent(
        locator=f'{locator}//*[@id="odds-filter"]'
    )  # ToDo: implement odds filter component

    def __init__(self) -> None:
        super().__init__(locator=self.locator)
