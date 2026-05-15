
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import os
import datetime


# ✅ Add CLI option
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="all",
        help="Browser to run: chrome / edge / firefox / all"
    )


# ✅ Browser fixture (supports ALL + single browser)
@pytest.fixture(params=["chrome", "edge", "firefox"])
def browser(request):
    selected_browser = request.config.getoption("--browser")

    if selected_browser != "all" and request.param != selected_browser:
        pytest.skip(f"Skipping {request.param}, running only {selected_browser}")

    return request.param


# ✅ Setup fixture
@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge browser......")

    elif browser == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        print("Launching Firefox browser......")

    else:
        driver = webdriver.Chrome()
        print("Launching Chrome browser......")

    driver.maximize_window()
    yield driver
    driver.quit()


# ✅ HTML report + metadata (FIXED - no _metadata error)
def pytest_configure(config):
    config.option.htmlpath = (
        os.path.abspath(os.curdir)
        + "\\reports\\"
        + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        + ".html"
    )


# ✅ Clean metadata (safe hook)
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("Plugins", None)
