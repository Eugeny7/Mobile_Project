import allure
from selenium.common import NoSuchElementException, TimeoutException
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, gender, locale, driver: WebDriver):
        self.driver = driver
        self.gender = gender
        self.locale = locale

    def send_a_value_to_the_field(self, element: tuple[str, str], field_value: str) -> None:
        """Заполнение поля по локатору"""
        field_input = self.get_clickable_element(element)
        field_input.send_keys(field_value)
        self.skip_dropdown_dadata()
        with allure.step('Проверка установленного значения в поле'):
            value_input = field_input.text
            assert value_input == field_value, f'Значение в проверяемом поле: {value_input} НЕ соответствует ожидаемому {field_value}'

    def get_clickable_element(self, locator):
        """Поиск кликабельного веб елемента по локатору"""
        wait = WebDriverWait(self.driver, 15, 2)
        try:
            element = wait.until(ec.element_to_be_clickable(locator))
        except TimeoutException:
            raise NoSuchElementException(f'Элемент с локатором {locator} не найден')
        return element

    def get_visible_element(self, locator):
        """Поиск видимого веб елемента по локатору"""
        wait = WebDriverWait(self.driver, 15, 2)
        try:
            element = wait.until(ec.visibility_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException(f'Элемент с локатором {locator} не найден')
        return element

    def swipe_vertical(self, direction: str) -> None:
        """Свайп экрана по вертикали, направление зависит от аргумента"""
        direction_normalized = direction.strip().lower()
        window = self.driver.get_window_size()
        start_x = window["width"] * 0.5
        if direction_normalized == 'up':
            start_y = window["height"] * 0.8
            end_y = window["height"] * 0.2
        elif direction_normalized == 'down':
            start_y = window["height"] * 0.2
            end_y = window["height"] * 0.8
        else:
            raise ValueError(f'Направление {direction} не поддерживается')
        finger = PointerInput("touch", "finger")
        actions = ActionBuilder(self.driver, mouse=finger)
        actions.pointer_action.move_to_location(start_x, start_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(0.2)
        actions.pointer_action.move_to_location(start_x, end_y)
        actions.pointer_action.pointer_up()
        actions.perform()

    def skip_dropdown_dadata(self) -> None:
        """Закрыть выпадающий список инпута от dadata """
        action = ActionChains(self.driver)
        action.send_keys(Keys.ENTER).perform()

    def activation_of_checkbox(self, element: tuple[str, str]) -> None:
        """Активация чекбокса по локатору"""
        item = self.get_clickable_element(element)
        if not item.get_attribute('checked') == 'true':
            item.click()
        with allure.step('Проверка состояния чек-бокса'):
            assert item.get_attribute('checked') == 'true', f'Чек-бокс НЕ активен'

    def deactivation_of_checkbox(self, element: tuple[str, str]) -> None:
        """Деактивация чекбокса по локатору"""
        item = self.get_clickable_element(element)
        if item.get_attribute('checked') == 'true':
            item.click()
        with allure.step('Проверка состояния чек-бокса'):
            assert item.get_attribute('checked') != 'true', f'Чек-бокс активен'
