from selenium.webdriver.common.by import By

from consts.constants import REGISTRATION_URL, BASE_URL
from locators.by_locators import ByLocators as BC
from utils.driver_utils import wait_element_is_visible, wait_element_is_not_visible


class TestAccountAccess:
    def test_access_to_account_click_sign_in_button(self, driver, random_user, registration):
        driver.get(url=REGISTRATION_URL)
        registration()

        wait_element_is_visible(driver, locator=BC.SIGN_IN_H2_TEXT)

        driver.find_element(By.XPATH, BC.SIGN_IN_EMAIL).send_keys(random_user.random_email)
        driver.find_element(By.XPATH, BC.SIGN_IN_PASSWORD).send_keys(random_user.random_password)
        enter_button = driver.find_element(By.XPATH, BC.SIGN_IN_BUTTON)
        enter_button.click()
        wait_element_is_not_visible(driver, element=enter_button)

        order_button = driver.find_element(By.XPATH, BC.SIGN_IN_ORDER_BUTTON)
        assert order_button.text == 'Оформить заказ'

    def test_access_to_account_press_personal_account_link(self, driver, random_user, registration):
        driver.get(url=REGISTRATION_URL)
        registration()

        link = driver.find_element(By.XPATH, BC.PERSONAL_ACCOUNT_LINK)
        driver.execute_script('arguments[0].click();', link)

        wait_element_is_visible(driver, locator=BC.SIGN_IN_H2_TEXT)

        driver.find_element(By.XPATH, BC.SIGN_IN_EMAIL).send_keys(random_user.random_email)
        driver.find_element(By.XPATH, BC.SIGN_IN_PASSWORD).send_keys(random_user.random_password)
        enter_button = driver.find_element(By.XPATH, BC.SIGN_IN_BUTTON)
        enter_button.click()
        wait_element_is_not_visible(driver, element=enter_button)

        order_button = driver.find_element(By.XPATH, BC.SIGN_IN_ORDER_BUTTON)
        assert order_button.text == 'Оформить заказ'

    def test_access_to_account_using_registration_link(self, driver, random_user, registration):
        driver.get(url=REGISTRATION_URL)
        registration()

        driver.get(url=BASE_URL)
        driver.find_element(By.XPATH, BC.SIGN_IN_ACCOUNT_BUTTON).click()
        wait_element_is_visible(driver, locator=BC.SIGN_IN_H2_TEXT)

        driver.find_element(By.XPATH, BC.REGISTRATION_LINK).click()
        wait_element_is_visible(driver, by=By.CSS_SELECTOR, locator='.undefined')

        enter_link = driver.find_element(By.XPATH, BC.SIGN_IN_LINK)
        driver.execute_script('arguments[0].click();', enter_link)
        wait_element_is_visible(driver, BC.SIGN_IN_H2_TEXT)

        driver.find_element(By.XPATH, BC.SIGN_IN_EMAIL).send_keys(random_user.random_email)
        driver.find_element(By.XPATH, BC.SIGN_IN_PASSWORD).send_keys(random_user.random_password)
        enter_button = driver.find_element(By.XPATH, BC.SIGN_IN_BUTTON)
        enter_button.click()
        wait_element_is_not_visible(driver, element=enter_button)

        order_button = driver.find_element(By.XPATH, BC.SIGN_IN_ORDER_BUTTON)
        assert order_button.text == 'Оформить заказ'

    def test_access_to_account_using_restore_password_link(self, driver, random_user, registration):
        driver.get(url=REGISTRATION_URL)
        registration()
        driver.get(url=BASE_URL)

        driver.find_element(By.XPATH, BC.SIGN_IN_ACCOUNT_BUTTON).click()
        wait_element_is_visible(driver, locator=BC.SIGN_IN_H2_TEXT)

        driver.find_element(By.XPATH, BC.RESTORE_PASSWORD_LINK).click()
        wait_element_is_visible(driver, locator=BC.RESTORE_PASSWORD_BUTTON)

        enter_link = driver.find_element(By.XPATH, BC.SIGN_IN_LINK)
        driver.execute_script('arguments[0].click();', enter_link)

        wait_element_is_visible(driver, locator=BC.SIGN_IN_H2_TEXT)

        driver.find_element(By.XPATH, BC.SIGN_IN_EMAIL).send_keys(random_user.random_email)
        driver.find_element(By.XPATH, BC.SIGN_IN_PASSWORD).send_keys(random_user.random_password)
        enter_button = driver.find_element(By.XPATH, BC.SIGN_IN_BUTTON)
        enter_button.click()
        wait_element_is_not_visible(driver, element=enter_button)

        order_button = driver.find_element(By.XPATH, BC.SIGN_IN_ORDER_BUTTON)
        assert order_button.text == 'Оформить заказ'
