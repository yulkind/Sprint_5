from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators


class TestLogin:
    def test_login_from_main_page(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.LOGIN_EMAIL)
        ).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        placing_order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PLACING_ORDER_BUTTON)
        ).text
        assert placing_order_button == 'Оформить заказ'

    def test_login_from_profile(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        placing_order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PLACING_ORDER_BUTTON)
        ).text
        assert placing_order_button == 'Оформить заказ'

    def test_login_through_registration_form(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        placing_order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PLACING_ORDER_BUTTON)
        ).text
        assert placing_order_button == 'Оформить заказ'

    def test_login_through_restore_password_form(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.RESTORE_PASSWORD_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        placing_order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PLACING_ORDER_BUTTON)
        ).text
        assert placing_order_button == 'Оформить заказ'
