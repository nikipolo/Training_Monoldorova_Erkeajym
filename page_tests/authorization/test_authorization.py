from page_objects.LoginPage import LoginPage
from vendor.Selenium.Chrome.WebDriver import WebDriver


def test_is_authorization(driver: WebDriver) -> None:
    """_summary_

    Args:
        driver (WebDriver): _description_
    """

    page: LoginPage = LoginPage(driver)
    page.open()

    assert page.driver().title == 'Авторизация', '[Заголовок] Мы не на странице авторизации.'


def test_authorization_empty_form(driver: WebDriver) -> None:
    """_summary_

    Args:
        driver (WebDriver): _description_
    """

    page: LoginPage = LoginPage(driver)
    page.open()
    page.set_username('')
    page.set_password('')
    page.click_on_submitter()

    assert page.driver().title == 'Авторизация', '[Заголовок] Мы не на странице авторизации.'
