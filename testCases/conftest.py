from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser...")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser...")
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):  # This will get the value from CLI / hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the Browser value to setup method
    return request.config.getoption("--browser")


########### Pytest HTML Report ###########

# Hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Aquib'

# Hook to delete/modify environment info in HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)