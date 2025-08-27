from mobile_project.Android_CTY.page.locators import *
import allure
from selenium.common import NoSuchElementException, TimeoutException
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    @allure.step('Поиск веб елемента')
    def get_element(self, locator):
        wait = WebDriverWait(self.driver, 15, 2)
        try:
            element = wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise NoSuchElementException(f'Элемент с локатором {locator} не найден')
        return element

    @allure.step('Проверка перехода на экран регистрации, шаг №1')
    def go_to_reg_page_step_one(self):
        self.get_element(BasePageLocators.on_boarding_fragment_skip).click()
        self.get_element(BasePageLocators.loan_btn_nav_bar).click()
        self.get_element(BasePageLocators.get_money_dialog_btn).click()
        with allure.step('Проверка заголовка текущего экрана'):
            title_window = self.get_element(RegPageLocatorsStepOne.title_window_step_one).text
            assert title_window == 'Регистрация', f'Переход НЕ осуществлён,текущий экран : {title_window}'
