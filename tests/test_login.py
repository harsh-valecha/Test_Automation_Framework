import pytest
from selenium import webdriver
from pages.login_page import LoginPage
# from pages.dashboard_page import DashboardPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    # dashboard_page = DashboardPage(driver)

    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    print('working fine ')
    # assert dashboard_page.is_dashboard_page()
