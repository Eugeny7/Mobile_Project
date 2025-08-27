from mimesis import Gender
import allure
from mobile_project.Android_CTY.page.locators import *
from mobile_project.Android_CTY.page.helper import Helper


class RegistrationStepOne(Helper):

    @allure.step('Проверка состоятния радиобаттона "Пол"')
    def choosing_gender_radiobaton(self):
        gender_normalized = self.gender.strip().lower()
        if gender_normalized == 'male':
            element = self.get_element(RegPageLocatorsStepOne.gender_male_radiobutton)
        elif gender_normalized == 'female':
            element = self.get_element(RegPageLocatorsStepOne.gender_female_radiobutton)
        else:
            raise ValueError(f'Выбранный пол: {self.gender} не поддерживается')
        with allure.step('Выбор радиобаттона, если не активен'):
            if not element.get_attribute('checked') == 'true':
                element.click()
        value = element.get_attribute('checked')
        assert value == 'true', f'Состояние радиобаттона "Пол" == {value}'

    @allure.step('Проверка состояния чек-бокса "Подписаться на рассылку')
    def choosing_sending_checkbox_if_not_selected(self):
        item = self.get_element(RegPageLocatorsStepOne.sending_checkbox)
        with allure.step('Клик по чек-боксу, если НЕ выбран'):
            if not item.get_attribute('checked') == 'true':
                item.click()
        assert item.get_attribute('checked') == 'true', f'Согласие на рассылку не предоставлено'

    @allure.step('Проверка состояния чек-бокса "Согласие на обработку ПДН')
    def choosing_consent_pdn_checkbox_if_not_selected(self):
        item = self.get_element(RegPageLocatorsStepOne.consent_pdn_checkbox)
        with allure.step('Клик по чек-боксу, если НЕ выбран'):
            if not item.get_attribute('checked') == 'true':
                item.click()
        assert item.get_attribute('checked') == 'true', f'Согласие на обработку ПДН не предоставлено'

    @allure.step('Проверка заполнения поля "Фамилия"')
    def should_be_filled_surname_input(self):
        user = self.generate_user()
        surname = self.get_element(RegPageLocatorsStepOne.surname_input)
        gender_normalized = self.gender.strip().lower()
        if gender_normalized == 'male':
            value_send = user.last_name(gender=Gender.MALE)
            surname.send_keys(value_send)
            self.driver.press_keycode(66)
        elif gender_normalized == 'female':
            value_send = user.last_name(gender=Gender.FEMALE)
            surname.send_keys(value_send)
            self.driver.press_keycode(66)
        else:
            raise ValueError(f'Выбранный пол: {self.gender} не поддерживается')
        value_input = surname.text
        assert value_input == value_send, f'Значение в поле "Фамилия" : {value_input} НЕ соответствует ожидаемому {value_send}'

    @allure.step('Проверка заполнения поля "Имя"')
    def should_be_filled_name_input(self):
        user = self.generate_user()
        name = self.get_element(RegPageLocatorsStepOne.name_input)
        gender_normalized = self.gender.strip().lower()
        if gender_normalized == 'male':
            value_send = user.first_name(gender=Gender.MALE)
            name.send_keys(value_send)
            self.driver.press_keycode(66)
        elif gender_normalized == 'female':
            value_send = user.first_name(gender=Gender.FEMALE)
            name.send_keys(value_send)
            self.driver.press_keycode(66)
        else:
            raise ValueError(f'Выбранный пол: {self.gender} не поддерживается')
        value_input = name.text
        assert value_input == value_send, f'Значение в поле "Имя": {value_input} НЕ соответствует ожидаемому {value_send}'

    @allure.step('Проверка заполнения поля "Отчество"')
    def should_be_filled_patronymic_input(self):
        user = self.generate_user()
        name_father = user.first_name()
        patronymic = self.get_element(RegPageLocatorsStepOne.patronymic_input)
        value_send = self.generate_patronymic(name_father)
        patronymic.send_keys(value_send)
        value_input = patronymic.text
        self.driver.press_keycode(66)
        assert value_input == value_send, f'Значение в поле "Отчество": {value_input} НЕ соответствует ожидаемому {value_send}'

    @allure.step('Проверка заполнения поля "Дата рождения"')
    def should_be_filled_birthday_input(self):
        value_send = self.generate_birthday(1990, 2006)
        date_of_birth = self.get_element(RegPageLocatorsStepOne.date_of_birth_input)
        date_of_birth.send_keys(value_send)
        value_input = date_of_birth.text
        assert value_input == value_send, f'Значение в поле "Дата рождения": {value_input} НЕ соответствует ожидаемому {value_send}'

    @allure.step('Проверка заполнения поля "Телефон"')
    def should_be_field_phone_input(self):
        user = self.generate_user()
        phone_field = self.get_element(RegPageLocatorsStepOne.phone_input)
        value_send = user.phone_number(mask='+7(9##)###-##-##', placeholder='#')
        phone_field.send_keys(value_send)
        value_input = phone_field.text
        assert value_input == value_send, f'Значение в поле "Телефон": {value_input} НЕ соответствует ожидаемому {value_send}'

    @allure.step('Проверка заполнения поля "E-mail"')
    def should_be_field_email_input(self):
        user = self.generate_user()
        email_field = self.get_element(RegPageLocatorsStepOne.email_input)
        value_send = user.email(unique=True)
        email_field.send_keys(value_send)
        value_input = email_field.text
        self.driver.press_keycode(66)
        assert value_input == value_send, f'Значение в поле "E-mail": {value_input} НЕ соответствует ожидаемому {value_send}'

    @allure.step('Проверка заполнения поля "Пароль"')
    def should_be_field_password_input(self):
        user = self.generate_user()
        password_field = self.get_element(RegPageLocatorsStepOne.password_input)
        value_send = user.password(length=6)
        password_field.send_keys(value_send)
        value_input = password_field.text
        assert value_input == value_send, f'Значение в поле "Пароль": {value_input} НЕ соответствует ожидаемому {value_send}'

    @allure.step('Проверка заполнения поля "Подтвердите пароль"')
    def should_be_field_password_confirm_input(self):
        password_confirm_field = self.get_element(RegPageLocatorsStepOne.password_confirm_input)
        value_send = self.get_element(RegPageLocatorsStepOne.password_input).text
        password_confirm_field.send_keys(value_send)
        value_input = password_confirm_field.text
        assert value_input == value_send, f'Значение в поле "Подтвердите пароль": {value_input} НЕ соответствует ожидаемому {value_send}'

    @allure.step('Проверка перехода на экран регистрации, шаг №2')
    def go_to_reg_page_step_two(self):
        self.get_element(RegPageLocatorsStepOne.registration_btn_next).click()
        title_window = self.get_element(RegPageLocatorsStepOne.title_window_step_two).text
        assert title_window == 'Документы и контакты', f'Переход НЕ осуществлён,текущий экран : {title_window}'
