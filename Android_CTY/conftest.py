import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from mobile_project.Android_CTY.page.base_page import BasePage
from mobile_project.Android_CTY.src.helper import Helper
from mobile_project.Android_CTY.page.reg_page import RegPageStepOne
from mobile_project.Android_CTY.page.onboarding_page import Onboarding

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    app='/Users/evgenijpuckov/apps/CTY-gms.apk',
    autoGrantPermissions=True,

)

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)


@pytest.fixture()
def driver():
    app = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield app
    app.quit()


@pytest.fixture()
def base_page(driver):
    return BasePage('female', 'ru', driver)


@pytest.fixture()
def helpers(driver):
    return Helper('female', 'ru', driver)


@pytest.fixture()
def reg_page(driver):
    return RegPageStepOne('female', 'ru', driver)


@pytest.fixture()
def onboarding_page(driver):
    return Onboarding('female', 'ru', driver)
