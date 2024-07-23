import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage


@pytest.fixture
def web_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_log_in(web_driver):
    login_page = LoginPage(web_driver)
    login_page.open_page()

    login_page.get_login_usernames()
    username_list = login_page.get_login_usernames().split('\n')
    username_list.pop(0)
    username = username_list[0]
    assert username == "standard_user"
    password_text = login_page.get_password().split('\n')
    password = password_text[1]

    login_page.write_on_username(username)
    login_page.write_on_password(password)
    login_page.click_on_login_button()

    products_page = ProductsPage(web_driver)
    product_titles = products_page.get_title_elements()
    print(product_titles)
