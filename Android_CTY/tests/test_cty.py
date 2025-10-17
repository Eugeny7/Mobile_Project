import allure
from mobile_project.Android_CTY.locators.locators import RegPageLocatorsStepTwo

@allure.title('Позитивная проверка первого шага регистрации')
def test_registration_step_one(pages, user):
    pages.onboarding.go_to_reg_page_step_one()
    pages.reg.fill_registration_step_one(user)
    pages.reg.go_to_reg_page_step_two()
    pages.helpers.assert_element_text(RegPageLocatorsStepTwo.title_window_step_two, 'Документы и контакты')
