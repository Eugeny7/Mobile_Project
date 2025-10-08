import allure


@allure.title('Позитивная проверка первого шага регистрации часть 2')
def test_registration_step_one(pages, user):
    pages.onboarding.go_to_reg_page_step_one()
    pages.reg.fill_registration_step_one(user)
    with allure.step('Переход на экран регистрации, шаг №2'):
        pages.reg.go_to_reg_page_step_two()
