import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TEST_EMAIL = "tatsiana_filimonenka_34-35_123@gmail.com"
TEST_PASSWORD = "practicum2026"

def login(driver, email, password):
    wait = WebDriverWait(driver, 10)
    
    email_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='name' and @type='text']")))
    email_input.clear()
    email_input.send_keys(email)
    
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    password_input.clear()
    password_input.send_keys(password)
    
    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]")
    login_button.click()

def test_login_from_main_page(driver):
    driver.get("https://stellarburgers.education-services.ru")
    wait = WebDriverWait(driver, 10)
    
    login_button_main = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Войти')]")))
    login_button_main.click()
    
    login(driver, TEST_EMAIL, TEST_PASSWORD)
    
    account_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '/account')]")))
    assert account_link.is_displayed()

def test_login_from_registration_form(driver):
    driver.get("https://stellarburgers.education-services.ru/register")
    wait = WebDriverWait(driver, 10)
    
    login_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Войти')]")))
    login_link.click()
    
    login(driver, TEST_EMAIL, TEST_PASSWORD)
    
    account_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '/account')]")))
    assert account_link.is_displayed()

def test_login_from_recovery_form(driver):
    driver.get("https://stellarburgers.education-services.ru/forgot-password")
    wait = WebDriverWait(driver, 10)
    
    login_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Войти')]")))
    login_link.click()
    
    login(driver, TEST_EMAIL, TEST_PASSWORD)
    
    account_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '/account')]")))
    assert account_link.is_displayed()

def test_login_from_personal_account(driver):
    driver.get("https://stellarburgers.education-services.ru")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/account')]"))).click()

    login(driver, TEST_EMAIL, TEST_PASSWORD)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/account')]"))).click()

    save_button = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='Сохранить']"))
    )

    assert save_button.is_displayed()
