from locators import Locators


class TestSwitchSectionsInConstructor:
    def test_switch_from_buns_to_sauces(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click(driver)
        switch_to_sauces = driver.find_element(Locators.SAUCES_BUTTON).text()
        assert switch_to_sauces == "Соусы"

    def test_switch_from_buns_to_fillings(self, driver):
        driver.find_element(*Locators.FILLINGS_BUTTON).click(driver)
        switch_to_fillings = driver.find_element(Locators.FILLINGS_BUTTON).text()
        assert switch_to_fillings == "Начинки"

    def test_switch_from_sauces_to_buns(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click(driver)
        driver.find_element(*Locators.BUNS_BUTTON).click(driver)
        switch_to_buns = driver.find_element(Locators.BUNS_BUTTON).text()
        assert switch_to_buns == "Булки"

    def test_switch_from_sauces_to_fillings(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click(driver)
        driver.find_element(*Locators.FILLINGS_BUTTON).click(driver)
        switch_to_fillings = driver.find_element(Locators.FILLINGS_BUTTON).text()
        assert switch_to_fillings == "Начинки"

    def test_switch_from_fillings_to_buns(self, driver):
        driver.find_element(*Locators.FILLINGS_BUTTON).click(driver)
        driver.find_element(*Locators.BUNS_BUTTON).click(driver)
        switch_to_buns = driver.find_element(Locators.BUNS_BUTTON).text()
        assert switch_to_buns == "Булки"

    def test_switch_from_fillings_to_sauces(self, driver):
        driver.find_element(*Locators.FILLINGS_BUTTON).click(driver)
        driver.find_element(*Locators.SAUCES_BUTTON).click(driver)
        switch_to_sauces = driver.find_element(Locators.SAUCES_BUTTON).text()
        assert switch_to_sauces == "Соусы"

