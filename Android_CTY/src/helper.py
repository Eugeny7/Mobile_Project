import json
import os
from mobile_project.Android_CTY.page.base_page import BasePage
from mimesis import Person
from mimesis.locales import Locale
from mimesis import Gender


class Helper(BasePage):

    def create_user(self, min_year: int, max_year: int):
        """Создание модели юзера и запись в отдельный файл"""
        if min_year <= 0 or max_year <= 0:
            raise ValueError('Год должен быть положительным числом')
        if min_year > max_year:
            raise ValueError(f'Минимальный год НЕ должен быть больше максимального года')
        user = self.generate_user_person(self.locale)
        value_surname = user.last_name(gender=self.resulting_gender(self.gender))
        value_name = user.first_name(gender=self.resulting_gender(self.gender))
        value_patronymic = self.generate_patronymic(self.gender, value_name)
        value_birthday = user.birthdate(min_year, max_year).strftime("%d/%m/%Y")
        value_phone = user.phone_number(mask='+7(9##)###-##-##', placeholder='#')
        value_email = user.email(unique=True)
        value_password = user.password(length=6)
        user_data = {
            'surname': value_surname,
            'name': value_name,
            'patronymic': value_patronymic,
            'birthday': value_birthday,
            'phone': value_phone,
            'email': value_email,
            'password': value_password
        }
        base_dir = "/Users/evgenijpuckov/PycharmProjects/QA_Auto_Appium/mobile_project/Android_CTY/src"
        file_path = os.path.join(base_dir, "user_data.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(user_data, f, ensure_ascii=False, indent=4)
        return user_data

    @staticmethod
    def generate_user_person(locale):
        """Генерация объекта класса Person"""
        locale_normalized = locale.strip().lower()
        if locale_normalized == 'ru':
            user = Person(Locale.RU)
        elif locale_normalized == 'en':
            user = Person(Locale.EN)
        else:
            raise ValueError(f'Выбранная локализация: {locale} не поддерживается')
        return user

    @staticmethod
    def generate_patronymic(gender, fathers_name) -> str:
        """Генерация отчества для модели юзера"""
        gender_normalized = gender.strip().lower()
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
            raise ValueError(f'Выбранный гендер: {gender} не поддерживается')
        return patronymic.capitalize()

    @staticmethod
    def resulting_gender(gender):
        """Получение гендера"""
        gender_data = {
            'male': Gender.MALE,
            'female': Gender.FEMALE
        }
        gender_normalized = gender.strip().lower()
        if gender_normalized not in gender_data:
            raise ValueError(f'Выбранный пол: {gender} не поддерживается')
        return gender_data[gender_normalized]

    @staticmethod
    def read_file_user(file_name):
        """Чтение файла по имени"""
        dir_path = '/Users/evgenijpuckov/PycharmProjects/QA_Auto_Appium/mobile_project/Android_CTY/src'
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, "r", encoding="utf-8") as f:
            user_data = json.load(f)
        return user_data

    def get_element_text(self, element: tuple[str, str]) -> str:
        title = self.get_visible_element(element)
        return title.text

    def is_element_selected(self, element: tuple[str, str]) -> bool:
        item = self.get_visible_element(element)
        value = item.get_attribute('checked')
        if value == 'true':
            return True
        else:
            return False

    def assert_element_text(self, element: tuple[str, str], expected_result):
        actual_result = self.get_element_text(element)
        assert actual_result == expected_result, f'Фактическое значение{actual_result} не соответствует ожидаемому{expected_result}значению'

    def assert_element_selected(self, element: tuple[str, str]) -> None:
        assert self.is_element_selected(element), f'Элемент {element} checkbox/radiobutton НЕ активирован'

    def clear_field(self, element: tuple[str, str])-> None:
        self.get_clickable_element(element).clear()
