
import allure
import pytest

from mobile_project.Android_CTY.locators.locators import RegPageLocatorsStepOne, RegPageLocatorsStepTwo


@allure.title('Позитивная проверка первого шага регистрации')
def test_registration_step_one(pages, user):
    pages.onboarding.go_to_reg_page_step_one()
    pages.reg.fill_registration_step_one(user)
    pages.reg.go_to_reg_page_step_two()
    pages.helpers.assert_element_text(RegPageLocatorsStepTwo.title_window_step_two, 'Документы и контакты')


@allure.title('Негативная проверка заполнения поля "Фамилия" первого шага регистрации')
@pytest.mark.parametrize('value',
                         ['123']
                         )
def test_field_surname_reg_step_one(pages, value):
    pages.onboarding.go_to_reg_page_step_one()
    pages.helpers.clear_field(RegPageLocatorsStepOne.surname_input)
    pages.base.send_a_value_to_the_field(RegPageLocatorsStepOne.surname_input, value)
    pages.helpers.assert_element_text(RegPageLocatorsStepOne.surname_input, 'Фамилия')

