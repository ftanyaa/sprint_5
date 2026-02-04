from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.auth import login
from helpers.credentials import TEST_EMAIL, TEST_PASSWORD
from helpers.urls import REGISTER_URL, FORGOT_PASSWORD_URL


def test_login_from_main_page(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Войти')]"))
    ).click()

    login(driver, TEST_EMAIL, TEST_PASSWORD)

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '/account')]"))
    )


def test_login_from_registration_form(driver):
    driver.get(REGISTER_URL)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Войти')]"))
    ).click()

    login(driver, TEST_EMAIL, TEST_PASSWORD)

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '/account')]"))
    )


def test_login_from_recovery_form(driver):
    driver.get(FORGOT_PASSWORD_URL)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Войти')]"))
    ).click()

    login(driver, TEST_EMAIL, TEST_PASSWORD)

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '/account')]"))
    )


def test_login_from_personal_account(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/account')]"))
    ).click()

    login(driver, TEST_EMAIL, TEST_PASSWORD)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/account')]"))
    ).click()

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='Сохранить']"))
    )
