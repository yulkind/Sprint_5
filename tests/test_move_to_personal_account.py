from locators import Locators

class TestMoveToPersonalAccount:
    def test_move_to_personal_account(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        login_button = driver.find_element(Locators.LOGIN_BUTTON).text()
        assert login_button == 'Войти'
