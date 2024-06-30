from selenium.webdriver.common.by import By


class Locators:
    # Регистрация аккаунта
    REG_LINK = (By.XPATH, '//a[@href="/register"]')
    REG_NAME = (By.XPATH, '//label[contains(text(),"Имя")]/following-sibling::input[@name="name"]')
    REG_EMAIL = (By.XPATH, '//label[contains(text(),"Email")]/following-sibling::input[@name="name"]')
    REG_PASSWORD = (By.XPATH, '//input[@type="password"]')
    REG_BUTTON = (By.CLASS_NAME, '//button[text() = "Зарегистрироваться"]')

    # Аутентификация
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')
    LOGIN_EMAIL = (By.XPATH, '//label[contains(text(),"Email")]/following-sibling::input[@name="name"]')
    LOGIN_PASSWORD = (By.XPATH, '//label[contains(text(),"Пароль")]/following-sibling::input[@name="Пароль"]')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    LOGIN_LINK = (By.XPATH, '//a[@href="/login"]')
    RESTORE_PASSWORD_LINK = (By.XPATH, '//a[@href="/forgot-password"]')

    # Главная страница
    PLACING_ORDER_BUTTON = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')
    BUNS_BUTTON = (By.XPATH, '//span[contains(text(),"Булки")]')
    SAUCES_BUTTON = (By.XPATH, '//span[contains(text(),"Соусы")]')
    FILLINGS_BUTTON = (By.XPATH, '//span[contains(text(),"Начинки")]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[contains(text(),"Конструктор")]')
    LOGO_BUTTON = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')

    # Личный кабинет
    PROFILE_BUTTON = (By.XPATH, '//p[(text()="Личный Кабинет")]')
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход")]')