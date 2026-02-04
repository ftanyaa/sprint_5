from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.auth import login
from helpers.credentials import TEST_EMAIL, TEST_PASSWORD
from helpers.urls import LOGIN_URL
from locators.locators import MainPageLocators


def test_go_to_personal_account(driver):
    driver.get(LOGIN_URL)
    login(driver, TEST_EMAIL, TEST_PASSWORD)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT)
    ).click()

    assert WebDriverWait(driver, 10).until(
        EC.url_contains("account")
    )


def test_logout(driver):
    driver.get(LOGIN_URL)
    login(driver, TEST_EMAIL, TEST_PASSWORD)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.LOGOUT_BUTTON)
    ).click()

    assert WebDriverWait(driver, 10).until(
        EC.url_contains("login")
    )


def test_go_to_constructor_from_account(driver):
    driver.get(LOGIN_URL)
    login(driver, TEST_EMAIL, TEST_PASSWORD)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
    ).click()

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
    )


def test_go_to_constructor_from_logo(driver):
    driver.get(LOGIN_URL)
    login(driver, TEST_EMAIL, TEST_PASSWORD)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.LOGO)
    ).click()

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
    )
