from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.auth import login
from helpers.credentials import TEST_EMAIL, TEST_PASSWORD
from helpers.urls import REGISTER_URL, FORGOT_PASSWORD_URL
from locators.locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators


def test_login_from_main_page(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
    ).click()

    login(driver, TEST_EMAIL, TEST_PASSWORD)

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT)
    )


def test_login_from_registration_form(driver):
    driver.get(REGISTER_URL)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_LINK)
    ).click()

    login(driver, TEST_EMAIL, TEST_PASSWORD)

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT)
    )


def test_login_from_recovery_form(driver):
    driver.get(FORGOT_PASSWORD_URL)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_LINK)
    ).click()

    login(driver, TEST_EMAIL, TEST_PASSWORD)

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT)
    )


def test_login_from_personal_account(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT)
    ).click()

    login(driver, TEST_EMAIL, TEST_PASSWORD)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT)
    ).click()

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.SAVE_BUTTON)
    )
