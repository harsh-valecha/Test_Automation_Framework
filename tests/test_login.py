import pytest
from selenium import webdriver
from pages.login import LoginPage
from pages.dashboard import DashboardPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    driver.implicitly_wait(10)
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    dashboard_page.search_dashboard('admin')
    dashboard_page.click_admin()
    assert dashboard_page.dashboard_page_title()=='Admin'


