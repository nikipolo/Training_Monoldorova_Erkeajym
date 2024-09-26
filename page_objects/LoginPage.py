from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.Browser import Browser
from config.settings import DOMAIN


class LoginPage(Browser):
    """_summary_

    Args:
        Browser (_type_): _description_
    """

    url: str = f'{DOMAIN}login'

    def open(self) -> None:
        """_summary_
        """

        self._driver.get(self.url)

    def set_username(self, username: str) -> None:
        """_summary_

        Args:
            username (str): _description_
        """

        (self._driver
            .wait()
            .until((EC.presence_of_element_located((By.CSS_SELECTOR, '#loginform-login'))))
            .send_keys(username))

    def set_password(self, password: str) -> None:
        """_summary_

        Args:
            password (str): _description_
        """

        (self._driver
            .wait()
            .until((EC.presence_of_element_located((By.CSS_SELECTOR, '#loginform-password'))))
            .send_keys(password))

    def click_on_submitter(self) -> None:
        """_summary_
        """

        (self._driver
            .wait()
            .until((EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))))
            .click())
