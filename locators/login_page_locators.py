from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "name")  
    PASSWORD_INPUT = (By.NAME, "Пароль")  
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  
    RECOVERY_LINK = (By.XPATH, "//a[text()='Восстановить пароль']") 