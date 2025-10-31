import allure
from mobile_project.Android_CTY.locators.locators import RegPageLocatorsStepOne
from mobile_project.Android_CTY.page.base_page import BasePage


class RegPageStepOne(BasePage):

    def choosing_gender_radiobaton(self) -> None:
        """Выбор радиобаттона 'Пол', в зав-ти от атрибута gender"""
        gender_normalized = self.gender.strip().lower()
        match gender_normalized:
            case 'male':
                element = self.get_clickable_element(RegPageLocatorsStepOne.gender_male_radiobutton)
            case 'female':
                element = self.get_clickable_element(RegPageLocatorsStepOne.gender_female_radiobutton)
            case _:
                raise ValueError(f'Выбранный пол: {self.gender} не поддерживается')
        if not element.get_attribute('checked') == 'true':
            element.click()

    def go_to_reg_page_step_two(self) -> None:
        """Переход на экран регистрации, шаг №2"""
        self.get_clickable_element(RegPageLocatorsStepOne.registration_btn_next).click()

    def fill_registration_step_one(self, user):
        with allure.step('Заполнение поля "Фамилия"'):
            self.send_a_value_to_the_field(RegPageLocatorsStepOne.surname_input, user["surname"])
        with allure.step('Заполнение поля "Имя"'):
            self.send_a_value_to_the_field(RegPageLocatorsStepOne.name_input, user["name"])
        with allure.step('Заполнение поля "Отчество"'):
            self.send_a_value_to_the_field(RegPageLocatorsStepOne.patronymic_input, user["patronymic"])
        with allure.step('Заполнение поля "Дата рождения"'):
            self.send_a_value_to_the_field(RegPageLocatorsStepOne.date_of_birth_input, user["birthday"])
        with allure.step('Выбор радиобаттона "Пол"'):
            self.choosing_gender_radiobaton()
        with allure.step('Заполнение поля "Телефон"'):
            self.send_a_value_to_the_field(RegPageLocatorsStepOne.phone_input, user["phone"])
        with allure.step('Заполнение поля "E-mail"'):
            self.send_a_value_to_the_field(RegPageLocatorsStepOne.email_input, user["email"])
        with allure.step('Заполнение поля "Пароль"'):
            self.send_a_value_to_the_field(RegPageLocatorsStepOne.password_input, user["password"])
        self.swipe_vertical('up')
        with allure.step('Заполнение поля "Подтвердите пароль"'):
            self.send_a_value_to_the_field(RegPageLocatorsStepOne.password_confirm_input, user["password"])
        with allure.step('Активация чек-бокса "Подписаться на рассылку"'):
            self.activation_of_checkbox(RegPageLocatorsStepOne.sending_checkbox)
        with allure.step('Активация чек-бокса "Согласие на обработку ПДН"'):
            self.activation_of_checkbox(RegPageLocatorsStepOne.consent_pdn_checkbox)
