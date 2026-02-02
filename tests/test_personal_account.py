from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.auth import login
from helpers.credentials import TEST_EMAIL, TEST_PASSWORD
from locators.locators import MainPageLocators


def test_go_to_personal_account(driver):
    login(driver, TEST_EMAIL, TEST_PASSWORD)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(
        EC.url_contains("account")
    )
    assert "account" in driver.current_url


def test_logout(driver):
    login(driver, TEST_EMAIL, TEST_PASSWORD)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.LOGOUT_BUTTON)
    )

    driver.find_element(*MainPageLocators.LOGOUT_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("login")
    )


def test_go_to_constructor_from_account(driver):
    login(driver, TEST_EMAIL, TEST_PASSWORD)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_BUTTON)
    )

    driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
        )
    )

def test_go_to_constructor_from_logo(driver):
    login(driver, TEST_EMAIL, TEST_PASSWORD)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.LOGO)
    )

    driver.find_element(*MainPageLocators.LOGO).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
        )
    )
