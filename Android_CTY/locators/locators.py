from appium.webdriver.common.appiumby import AppiumBy


class OnboardingPageLocators:
    on_boarding_fragment_skip = (AppiumBy.ID, 'ru.cashtoyou.app:id/on_boarding_fragment_skip')
    get_money_dialog_btn = (AppiumBy.ID, 'ru.cashtoyou.app:id/get_money_dialog_progress_button_btn')
    loan_btn_nav_bar = (AppiumBy.ID, 'ru.cashtoyou.app:id/loanFragment')


class RegPageLocatorsStepOne:
    surname_input = (
    AppiumBy.XPATH, '(//android.widget.AutoCompleteTextView[@resource-id="ru.cashtoyou.app:id/input_value"])[1]')
    name_input = (
        AppiumBy.XPATH, '(//android.widget.AutoCompleteTextView[@resource-id="ru.cashtoyou.app:id/input_value"])[2]')
    patronymic_input = (
        AppiumBy.XPATH, '(//android.widget.AutoCompleteTextView[@resource-id="ru.cashtoyou.app:id/input_value"])[3]')
    date_of_birth_input = (
        AppiumBy.XPATH, '(//android.widget.AutoCompleteTextView[@resource-id="ru.cashtoyou.app:id/input_value"])[4]')
    phone_input = (
        AppiumBy.XPATH, '(//android.widget.AutoCompleteTextView[@resource-id="ru.cashtoyou.app:id/input_value"])[5]')
    email_input = (
        AppiumBy.XPATH, '(//android.widget.AutoCompleteTextView[@resource-id="ru.cashtoyou.app:id/input_value"])[6]')
    password_input = (AppiumBy.ID, 'ru.cashtoyou.app:id/password_input_field')
    password_confirm_input = (
        AppiumBy.XPATH, '(//android.widget.AutoCompleteTextView[@resource-id="ru.cashtoyou.app:id/input_value"])[4]')
    gender_male_radiobutton = (AppiumBy.ID, 'ru.cashtoyou.app:id/male')
    gender_female_radiobutton = (AppiumBy.ID, 'ru.cashtoyou.app:id/female')
    sending_checkbox = (
        AppiumBy.XPATH, '(//android.widget.CheckBox[@resource-id="ru.cashtoyou.app:id/material_cb_cb"])[1]')
    consent_pdn_checkbox = (
        AppiumBy.XPATH, '(//android.widget.CheckBox[@resource-id="ru.cashtoyou.app:id/material_cb_cb"])[2]')
    title_window_step_one = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Регистрация")')
    registration_btn_next = (AppiumBy.ID, 'ru.cashtoyou.app:id/registration_button_next')
    title_window_step_two = (AppiumBy.XPATH, '//android.widget.TextView[@text="Документы и контакты"]')
