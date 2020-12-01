from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching chrome browser..............")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print(("Launching firefox browser.............."))
    else:
        driver = webdriver.Ie(IEDriverManager().install())

        print("pass browser")

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#######Pytest HTML Report############

#it is hook for Adding Environment into to HTML report
def pytest_configure(config):
    config._metadata['Project Name']= 'nop commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Lavanya'

#It is hook for delete/Modify Environmenet info to HTML report
@pytest.mark.optionalhook
def pytest_metadat(metadata):
    metadata.pop("java_HOME",None)
    metadata.pop("Plugins",None)

