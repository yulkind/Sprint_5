from constants import Constants
from locators import Locators

class TestLogout:
    def logout_from_personal_account(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        login_button = driver.find_element(Locators.LOGIN_BUTTON).text()
        assert login_button == 'Войти'
