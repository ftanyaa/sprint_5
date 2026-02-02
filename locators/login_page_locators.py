from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "name")  # поле email
    PASSWORD_INPUT = (By.NAME, "Пароль")  # поле пароль
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # кнопка войти
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # ссылка "Войти" на странице регистрации
    RECOVERY_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # ссылка восстановление пароля
