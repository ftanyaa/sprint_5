from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page_locators import LoginPageLocators
from locators.locators import MainPageLocators

def login(driver, email, password):
    driver.get("https://stellarburgers.education-services.ru/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT))
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT))
