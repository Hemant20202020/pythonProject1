import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Platform")
    metadata.pop("Packages")
    metadata.pop("Plugins")
    metadata.pop("JAVA_HOME")

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    if hasattr(session.config, "_metadata"):
        session.config._metadata["Project Name"] = "Mercury"
