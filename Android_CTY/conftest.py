import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

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
