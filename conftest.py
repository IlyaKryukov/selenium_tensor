import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
    #chromeOptions.add_argument('headless')
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

