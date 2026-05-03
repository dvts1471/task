
from core.ui.pages import BasePage
from main.ui.components.bet_slip import BetSlip
from main.ui.components.filter_row import FilterRow
from main.ui.components.header import Header
from main.ui.components.match_list import MatchList
from main.ui.components.successful_receipt_pop_up import SuccessfulReceiptPopUp


class DashboardPage(BasePage):
    header = Header()
    filter_row = FilterRow()
    match_list = MatchList()
    bet_slip = BetSlip()
    successful_receipt_pop_up = SuccessfulReceiptPopUp()

    def wait_loaded(self, timeout: int = 5) -> 'DashboardPage':
        self.header.wait_element(timeout=timeout)
        self.match_list.wait_element(timeout=timeout)
        return self


