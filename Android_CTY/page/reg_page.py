import allure
from mobile_project.Android_CTY.locators.locators import RegPageLocatorsStepOne
from mobile_project.Android_CTY.page.base_page import BasePage


class RegPageStepOne(BasePage):

    def choosing_gender_radiobaton(self) -> None:
        """Выбор радиобаттона 'Пол', в зав-ти от атрибута gender"""
        gender_normalized = self.gender.strip().lower()
        if gender_normalized == 'male':
            element = self.get_clickable_element(RegPageLocatorsStepOne.gender_male_radiobutton)
        elif gender_normalized == 'female':
            element = self.get_clickable_element(RegPageLocatorsStepOne.gender_female_radiobutton)
        else:
            raise ValueError(f'Выбранный пол: {self.gender} не поддерживается')
        if not element.get_attribute('checked') == 'true':
            element.click()
        with allure.step('Проверка состояния радиобаттона'):
            value = element.get_attribute('checked')
            assert value == 'true', f'Состояние радиобаттона "Пол" == {value}'

    def go_to_reg_page_step_two(self) -> None:
        """Переход на экран регистрации, шаг №2"""
        self.get_clickable_element(RegPageLocatorsStepOne.registration_btn_next).click()
        with allure.step('Проверка заголовка текущего экрана'):
            title_window = self.get_clickable_element(RegPageLocatorsStepOne.title_window_step_two).text
            assert title_window == 'Документы и контакты', f'Переход НЕ осуществлён,текущий экран : {title_window}'
