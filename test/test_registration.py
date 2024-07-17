import pytest
from selenium.webdriver.common.by import By

from consts.constants import BASE_URL
from locators.by_locators import ByLocators as BC
from utils.driver_utils import wait_element_is_visible, wait_element_is_not_visible, wait_element_is_clickable


@pytest.mark.usefixtures("driver")
class TestRegistration:
    def test_success_registration(self, driver, random_user):
        driver.get(url=BASE_URL)

        driver.find_element(By.XPATH, BC.SIGN_IN_ACCOUNT_BUTTON).click()

        wait_element_is_visible(driver, locator=BC.SIGN_IN_H2_TEXT)

        driver.find_element(By.XPATH, BC.REGISTRATION_LINK).click()
        registration_element = wait_element_is_visible(driver, locator=BC.REGISTRATION_H2_TEXT)

        driver.find_element(By.XPATH, BC.REGISTRATION_NAME_INPUT).send_keys(random_user.username)
        driver.find_element(By.XPATH, BC.REGISTRATION_EMAIL_INPUT).send_keys(random_user.random_email)
        driver.find_element(By.XPATH, BC.REGISTRATION_PASSWORD_INPUT).send_keys(random_user.random_password)
        driver.find_element(By.XPATH, BC.REGISTRATION_BUTTON).click()

        wait_element_is_not_visible(driver, element=registration_element)

        element = wait_element_is_visible(driver, by=By.TAG_NAME, locator='h2')
        assert element.text == 'Вход'

    def test_registration_with_incorrect_password(self, driver, random_user):
        incorrect_password = '123'
        driver.get(url=BASE_URL)

        driver.find_element(By.XPATH, BC.SIGN_IN_ACCOUNT_BUTTON).click()
        wait_element_is_visible(driver, BC.SIGN_IN_H2_TEXT)

        driver.find_element(By.XPATH, BC.REGISTRATION_LINK).click()

        wait_element_is_clickable(driver, locator=BC.REGISTRATION_H2_TEXT)

        driver.find_element(By.XPATH, BC.REGISTRATION_NAME_INPUT).send_keys(random_user.username)
        driver.find_element(By.XPATH, BC.REGISTRATION_EMAIL_INPUT).send_keys(random_user.random_email)
        driver.find_element(By.XPATH, BC.REGISTRATION_PASSWORD_INPUT).send_keys(incorrect_password)
        driver.find_element(By.XPATH, BC.REGISTRATION_BUTTON).click()

        element = wait_element_is_visible(driver, by=By.CSS_SELECTOR, locator='.input__error')
        assert element.text == 'Некорректный пароль'
