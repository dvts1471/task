import threading
from typing import Any

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class DriverManager:
    _thread_local = threading.local()


    @property
    def driver(self) -> webdriver.Chrome:
        if not self.__get_driver():
            self.__create_driver()
        return self.__get_driver()

    @classmethod
    def __create_driver(cls) -> None:
        driver_path = ChromeDriverManager().install()
        service = webdriver.ChromeService(driver_path)
        cls._thread_local._driver = webdriver.Chrome(service=service)

    @classmethod
    def __get_driver(cls) -> Any:
        return getattr(cls._thread_local, '_driver', None)

    @classmethod
    def is_driver_initiated(cls) -> bool:
        return True if cls.__get_driver() else False

    @classmethod
    def close_driver(cls) -> None:
        if cls.__get_driver():
            cls.__get_driver().close()
            cls._thread_local._driver = None