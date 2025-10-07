import allure
from mobile_project.Android_CTY.locators.locators import RegPageLocatorsStepOne


@allure.title('Позитивная проверка первого шага регистрации часть 2')
def test_registration_step_one(base_page, reg_page, onboarding_page, helpers):
    with allure.step('Создание тестового пользователя'):
        helpers.create_user(1980, 2000)
        user = helpers.read_file_user('user_data.json')
    with allure.step('Переход на экран регистрации, шаг №1'):
        onboarding_page.go_to_reg_page_step_one()
    with allure.step('Заполнение поля "Фамилия"'):
        base_page.send_a_value_to_the_field(RegPageLocatorsStepOne.surname_input, user["surname"])
    with allure.step('Заполнение поля "Имя"'):
        base_page.send_a_value_to_the_field(RegPageLocatorsStepOne.name_input, user["name"])
    with allure.step('Заполнение поля "Отчество"'):
        base_page.send_a_value_to_the_field(RegPageLocatorsStepOne.patronymic_input, user["patronymic"])
    with allure.step('Заполнение поля "Дата рождения"'):
        base_page.send_a_value_to_the_field(RegPageLocatorsStepOne.date_of_birth_input, user["birthday"])
    with allure.step('Выбор радиобаттона "Пол"'):
        reg_page.choosing_gender_radiobaton()
    with allure.step('Заполнение поля "Телефон"'):
        base_page.send_a_value_to_the_field(RegPageLocatorsStepOne.phone_input, user["phone"])
    with allure.step('Заполнение поля "E-mail"'):
        base_page.send_a_value_to_the_field(RegPageLocatorsStepOne.email_input, user["email"])
    with allure.step('Заполнение поля "Пароль"'):
        base_page.send_a_value_to_the_field(RegPageLocatorsStepOne.password_input, user["password"])
    base_page.swipe_vertical('up')
    with allure.step('Заполнение поля "Подтвердите пароль"'):
        base_page.send_a_value_to_the_field(RegPageLocatorsStepOne.password_confirm_input, user["password"])
    with allure.step('Активация чек-бокса "Подписаться на рассылку"'):
        base_page.activation_of_checkbox(RegPageLocatorsStepOne.sending_checkbox)
    with allure.step('Активация чек-бокса "Согласие на обработку ПДН"'):
        base_page.activation_of_checkbox(RegPageLocatorsStepOne.consent_pdn_checkbox)
    with allure.step('Переход на экран регистрации, шаг №2'):
        reg_page.go_to_reg_page_step_two()
