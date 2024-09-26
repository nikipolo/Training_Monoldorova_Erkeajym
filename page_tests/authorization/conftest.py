from pathlib import Path

from pytest import fixture
from undetected_chromedriver import ChromeOptions

from config import settings
from vendor.Selenium.Chrome.WebDriver import WebDriver


@fixture(scope='function')
def driver():
    """_summary_

    Yields:
        _type_: _description_
    """

    dir: Path = settings.STORAGE_BROWSER_DIR

    options: ChromeOptions = ChromeOptions()
    options.add_argument('--lang=ru-RU')
    options.add_argument('--accept-lang=ru-RU')
    options.add_argument('--user-agent=Selenium')
    # options.add_argument('--headless=new')

    driver: WebDriver = WebDriver(options=options, user_data_dir=dir)
    yield driver
    driver.quit()
