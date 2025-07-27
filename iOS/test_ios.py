from appium.webdriver.common.appiumby import AppiumBy
from  Otus.Appium.iOS.src import Helper
import allure

@allure.title('Создание события')
def test_contacts_app(driver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Automation').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'New Automation').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Alarm').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Goes Off').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Next').click()
    input_search = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Search')
    input_search.click()
    input_search.send_keys('Speak Text')
    driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Speak Text"]').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Done').click()
    element = driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeCell')
    help = Helper(driver)
    help.swipe_left_on_element(element, element.size['width'])
