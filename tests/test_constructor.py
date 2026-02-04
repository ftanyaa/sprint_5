from locators.locators import ConstructorLocators


def test_switch_to_buns(driver):
    driver.find_element(*ConstructorLocators.SAUCES).click()
    driver.find_element(*ConstructorLocators.BUNS).click()
    assert "Булки" in driver.find_element(*ConstructorLocators.ACTIVE_TAB).text


def test_switch_to_sauces(driver):
    driver.find_element(*ConstructorLocators.SAUCES).click()
    assert "Соусы" in driver.find_element(*ConstructorLocators.ACTIVE_TAB).text


def test_switch_to_fillings(driver):
    driver.find_element(*ConstructorLocators.FILLINGS).click()
    assert "Начинки" in driver.find_element(*ConstructorLocators.ACTIVE_TAB).text