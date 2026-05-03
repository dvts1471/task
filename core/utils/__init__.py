import os
import re
from typing import Union, List

import allure

from core.utils.driver_manager import DriverManager
from core.utils.logger import Logger


counter = 0

def get_current_test_name() -> str:
    test_full_name: str | None = os.environ.get('PYTEST_CURRENT_TEST')
    if test_full_name is None:
        return ""
    match = re.search('::(\w+)\s', test_full_name)
    if match:
        return match.group(1)
    return ""


@allure.step("Verify")
def verify(check: Union[List[bool], bool], f_msg: str, p_msg: str = '') -> None:
    global counter
    driver = DriverManager().driver
    logger = Logger("Verification")
    screenshot = driver.get_screenshot_as_png()
    allure.attach(
        screenshot,
        name=f"Screenshot_{counter}",
        attachment_type=allure.attachment_type.PNG
    )

    if isinstance(check, bool):
        check = [check]
    assert all(check), f_msg
    counter += 1
    logger.info(f'Verified: {p_msg}')