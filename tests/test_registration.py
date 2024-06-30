from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators

faker = Faker()

class TestRegistration:
    def test_successful_registration(self, driver):
        name = faker.name()
        email = faker.email()
        password = '123456'
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.REG_NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        login_message = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_LINK)).text
        assert login_message == 'Зарегистрироваться'

    def test_registration_with_incorrect_password(self, driver):
        name = faker.name()
        email = faker.email()
        password = '12345'
        driver.find_element(By.XPATH, '//nav/a/p[@class="AppHeader_header__linkText__3q_va ml-2"]').click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.REG_NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        incorrect_password_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//p[@class="input__error text_type_main-default"]'))).text
        assert incorrect_password_message == 'Некорректный пароль'
