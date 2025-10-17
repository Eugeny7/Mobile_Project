from mobile_project.Android_CTY.locators.locators import OnboardingPageLocators, RegPageLocatorsStepOne
from mobile_project.Android_CTY.page.base_page import BasePage
import allure


class Onboarding(BasePage):
    def go_to_reg_page_step_one(self) -> None:
        """Скип онбординга, переход на экран регистрации"""
        self.get_clickable_element(OnboardingPageLocators.on_boarding_fragment_skip).click()
        self.get_clickable_element(OnboardingPageLocators.loan_btn_nav_bar).click()
        self.get_clickable_element(OnboardingPageLocators.get_money_dialog_btn).click()
