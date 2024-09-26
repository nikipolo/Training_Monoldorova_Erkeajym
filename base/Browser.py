from abc import ABC

from vendor.Selenium.Chrome.WebDriver import WebDriver


class Browser(ABC):
    """_summary_
    """

    _driver: WebDriver

    def __init__(self, driver: WebDriver) -> None:
        """_summary_

        Args:
            driver (WebDriver): _description_
        """

        self._driver = driver

    def driver(self) -> WebDriver:
        """_summary_

        Returns:
            WebDriver: _description_
        """

        return self._driver
