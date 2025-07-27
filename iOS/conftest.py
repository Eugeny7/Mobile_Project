import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions

capabilities = dict(
    platformName='iOS',
    platformVersion='17.0',
    deviceName='iPhone 15 Plus',
    automationName='XCUITest',
    app='/Library/Developer/CoreSimulator/Volumes/iOS_21A342/Library/Developer/CoreSimulator/Profiles/Runtimes/iOS 17.0.simruntime/Contents/Resources/RuntimeRoot/Applications/Shortcuts.app',
    noReset=True

)

appium_server_url = 'http://localhost:4723'
capabilities_options = XCUITestOptions().load_capabilities(capabilities)


@pytest.fixture()
def driver():
    app = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield app
    app.quit()
