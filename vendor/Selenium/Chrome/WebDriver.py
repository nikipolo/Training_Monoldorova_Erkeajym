from selenium.webdriver.support.wait import WebDriverWait
from undetected_chromedriver import Chrome


class WebDriver(Chrome):
    """_summary_

    Args:
        Chrome (_type_): _description_
    """

    def wait(self, timeout: float = 10) -> WebDriverWait:
        """_summary_

        Args:
            timeout (float, optional): _description_. Defaults to 10.

        Returns:
            WebDriverWait: _description_
        """

        return WebDriverWait(self, timeout=timeout)
