import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to run tests on: chrome or firefox"
    )

@pytest.fixture(scope="module")
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Browser {browser} is not supported.")
    
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
