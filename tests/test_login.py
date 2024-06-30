from locators import Locators


class TestLogin:
    def test_login_from_main_page(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(driver)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(driver)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        placing_order_button = driver.find_element(Locators.PLACING_ORDER_BUTTON).text()
        assert placing_order_button == 'Оформить заказ'

    def test_login_from_profile(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(driver)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(driver)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        placing_order_button = driver.find_element(Locators.PLACING_ORDER_BUTTON).text()
        assert placing_order_button == 'Оформить заказ'

    def test_login_through_registration_form(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(driver)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(driver)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        placing_order_button = driver.find_element(Locators.PLACING_ORDER_BUTTON).text()
        assert placing_order_button == 'Оформить заказ'

    def test_login_through_restore_password_form(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.RESTORE_PASSWORD_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(driver)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(driver)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        placing_order_button = driver.find_element(Locators.PLACING_ORDER_BUTTON).text()
        assert placing_order_button == 'Оформить заказ'
