import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from mobile_project.Android_CTY.page.base_page import BasePage
from mobile_project.Android_CTY.src.helper import Helper
from mobile_project.Android_CTY.page.reg_page import RegPageStepOne
from mobile_project.Android_CTY.page.onboarding_page import Onboarding

capabilities = dict(
    platformName='Android',
    automationName='UiAutomator2',
    deviceName='emulator-5554',
    app='/Users/evgenijpuckov/apps/CTY-gms.apk',
    autoGrantPermissions=True,
    noReset=False
)

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)


@pytest.fixture(scope='function')
def driver():
    app = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield app
    app.quit()


class PageFactory:
    def __init__(self, driver, gender='male', locale='ru'):
        self.base = BasePage(gender, locale, driver)
        self.reg = RegPageStepOne(gender, locale, driver)
        self.onboarding = Onboarding(gender, locale, driver)
        self.helpers = Helper(gender, locale, driver)


@pytest.fixture()
def pages(driver):
    return PageFactory(driver)


@pytest.fixture()
def user(pages):
    pages.helpers.create_user(1980, 2000)
    user = pages.helpers.read_file_user('user_data.json')
    return user
