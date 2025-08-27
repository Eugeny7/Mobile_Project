import allure

@allure.title('Позитивная проверка первого шага регистрации')
def test_registration_step_one(base_page, reg_page, helpers):
    base_page.go_to_reg_page_step_one()
    reg_page.should_be_filled_surname_input()
    reg_page.should_be_filled_name_input()
    reg_page.should_be_filled_patronymic_input()
    reg_page.should_be_filled_birthday_input()
    reg_page.choosing_gender_radiobaton()
    reg_page.should_be_field_phone_input()
    reg_page.should_be_field_email_input()
    reg_page.should_be_field_password_input()
    helpers.swipe_up()
    reg_page.should_be_field_password_confirm_input()
    reg_page.choosing_sending_checkbox_if_not_selected()
    reg_page.choosing_consent_pdn_checkbox_if_not_selected()
    reg_page.go_to_reg_page_step_two()
