from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import RegistrationPageLocators
from helpers.generators import generate_email, generate_password
from helpers.urls import REGISTER_URL


def test_success_registration(driver):
    driver.get(REGISTER_URL)

    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Tatsiana")
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(generate_password())
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    assert WebDriverWait(driver, 10).until(
        EC.url_contains("login")
    )


def test_registration_with_short_password(driver):
    driver.get(REGISTER_URL)

    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Tatsiana")
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("123")
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_ERROR)
    )
