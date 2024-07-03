from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestRegistration:
    def test_successful_registration(self, faker, driver):
        name = faker.name()
        email = faker.email()
        password = '123456'
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.REG_NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.REG_BUTTON)).click()
        login_message = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_LINK)).text
        assert login_message == 'Зарегистрироваться'

    def test_registration_with_incorrect_password(self, faker, driver):
        name = faker.name()
        email = faker.email()
        password = '12345'
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.REG_NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        incorrect_password_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Locators.INCORRECT_PASSWORD_MESSAGE))).text
        assert incorrect_password_message == 'Некорректный пароль'
