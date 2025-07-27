from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

on_boarding_fragment_skip = (AppiumBy.ID, 'ru.cashtoyou.app:id/on_boarding_fragment_skip')
get_money_dialog_btn = (AppiumBy.ID, 'ru.cashtoyou.app:id/get_money_dialog_progress_button_btn')

def test_gmail(driver):
    wait = WebDriverWait(driver, 30, 1)
    wait.until(EC.visibility_of_element_located(on_boarding_fragment_skip)).click()
    wait.until(EC.element_to_be_clickable(get_money_dialog_btn)).click()