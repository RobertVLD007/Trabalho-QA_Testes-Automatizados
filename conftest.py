from pytest import fixture
from selenium import webdriver


@fixture
def browser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    #driver.maximize_window()

    yield driver

    driver.quit()
