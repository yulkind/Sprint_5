from locators import Locators


class TestSwitchToConstructor:
    def test_switch_to_constructor_from_personal_account_with_constructor_button(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        login_to_account_button = driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).text
        assert login_to_account_button == 'Войти в аккаунт'

    def test_switch_to_constructor_from_personal_account_with_logo_button(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.LOGO_BUTTON).click()
        login_to_account_button = driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).text
        assert login_to_account_button == 'Войти в аккаунт'