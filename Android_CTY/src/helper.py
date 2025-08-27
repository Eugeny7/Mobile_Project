import allure
from appium.webdriver.webdriver import WebDriver

from mobile_project.Android_CTY.page.base_page import BasePage
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from mimesis import Person
from mimesis.locales import Locale


class Helper(BasePage):
    def __init__(self, gender, locale, driver: WebDriver):
        super().__init__(driver)
        self.gender = gender
        self.locale = locale

    @allure.step('Генерация модели пользователя')
    def generate_user(self):
        locale_normalized = self.locale.strip().lower()
        if locale_normalized == 'ru':
            user = Person(Locale.RU)
        elif locale_normalized == 'en':
            user = Person(Locale.EN)
        else:
            raise ValueError(f'Выбранная локализация: {self.locale} не поддерживается')
        return user

    @allure.step('Генерация отчества')
    def generate_patronymic(self, fathers_name) -> str:
        gender_normalized = self.gender.strip().lower()
        fathers_name_normalized = fathers_name.strip().lower()
        if gender_normalized == 'male':
            if fathers_name_normalized.endswith('й'):
                patronymic = fathers_name_normalized[:-1] + 'евич'
            elif fathers_name_normalized.endswith('а'):
                patronymic = fathers_name_normalized[:-1] + 'ич'
            else:
                patronymic = fathers_name_normalized + 'ович'
        elif gender_normalized == 'female':
            if fathers_name_normalized.endswith('й'):
                patronymic = fathers_name_normalized[:-1] + 'евна'
            elif fathers_name_normalized.endswith('а'):
                patronymic = fathers_name_normalized[:-1] + 'ична'
            else:
                patronymic = fathers_name_normalized + 'овна'
        else:
            raise ValueError(f'Выбранный гендер: {self.gender} не поддерживается')
        return patronymic.capitalize()

    @allure.step('Генерация даты рождения')
    def generate_birthday(self, min_year: int, max_year: int):
        if min_year <= 0 or max_year <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        if min_year > max_year:
            raise ValueError("Минимальный возраст НЕ должен быть больше максимального возраста")
        user = self.generate_user()
        birthday = user.birthdate(min_year=min_year, max_year=max_year)
        return birthday.strftime("%d/%m/%Y")

    @allure.step('Cвайп экрана вверх')
    def swipe_up(self):
        window = self.driver.get_window_size()
        finger = PointerInput("touch", "finger")
        actions = ActionBuilder(self.driver, mouse=finger)
        start_x = window["width"] * 0.5
        start_y = window["height"] * 0.8
        end_y = window["height"] * 0.2
        actions.pointer_action.move_to_location(start_x, start_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(0.1)
        actions.pointer_action.move_to_location(start_x, end_y)
        actions.pointer_action.pointer_up()
        actions.perform()
