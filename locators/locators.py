from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class,'Account_button')]")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]")

    
class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    PASSWORD_ERROR = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")

class PersonalAccountLocators:
    LOGOUT = (By.XPATH, "//button[text()='Выход']")

class ConstructorLocators:
    BUNS = (By.XPATH, "//span[text()='Булки']")
    SAUCES = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS = (By.XPATH, "//span[text()='Начинки']")
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]")

class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "name")  
    PASSWORD_INPUT = (By.NAME, "Пароль") 
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")