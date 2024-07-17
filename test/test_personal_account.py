from selenium.webdriver.common.by import By

from consts.constants import BASE_URL, REGISTRATION_URL
from locators.by_locators import ByLocators as BC
from utils.driver_utils import wait_element_is_visible, wait_element_is_not_visible, wait_element_is_present


class TestPersonalAccount:
    def test_go_to_personal_account_authorized_user(self, driver, random_user, registration):
        driver.get(url=REGISTRATION_URL)
        registration()

        driver.get(url=BASE_URL)
        driver.find_element(By.XPATH, BC.SIGN_IN_ACCOUNT_BUTTON).click()
        wait_element_is_visible(driver, locator=BC.SIGN_IN_H2_TEXT)

        driver.find_element(By.XPATH, BC.SIGN_IN_EMAIL).send_keys(random_user.random_email)
        driver.find_element(By.XPATH, BC.SIGN_IN_PASSWORD).send_keys(random_user.random_password)
        enter_button = driver.find_element(By.XPATH, BC.SIGN_IN_BUTTON)
        enter_button.click()
        wait_element_is_not_visible(driver, element=enter_button)

        account_link = driver.find_element(By.XPATH, BC.PROFILE_LINK)
        driver.execute_script('arguments[0].click();', account_link)

        wait_element_is_present(driver, by=By.CSS_SELECTOR, locator='.input__textfield')
        account = driver.find_elements(By.CSS_SELECTOR, '.input__textfield')[0]

        assert account.get_property('value') == random_user.username

    def test_go_from_personal_account_to_constructor_clicking_by_logo(self, driver, random_user, registration):
        driver.get(url=REGISTRATION_URL)
        registration()

        driver.get(url=BASE_URL)
        driver.find_element(By.XPATH, BC.SIGN_IN_ACCOUNT_BUTTON).click()
        wait_element_is_visible(driver, locator=BC.SIGN_IN_H2_TEXT)

        driver.find_element(By.XPATH, BC.SIGN_IN_EMAIL).send_keys(random_user.random_email)
        driver.find_element(By.XPATH, BC.SIGN_IN_PASSWORD).send_keys(random_user.random_password)
        enter_button = driver.find_element(By.XPATH, BC.SIGN_IN_BUTTON)
        enter_button.click()
        wait_element_is_not_visible(driver, element=enter_button)

        link = driver.find_element(By.XPATH, BC.PERSONAL_ACCOUNT_LINK)
        driver.execute_script('arguments[0].click();', link)

        wait_element_is_present(driver, by=By.CSS_SELECTOR, locator='.input__textfield')

        driver.find_element(By.XPATH, BC.LOGO_BUTTON_LINK).click()
        construct_burger = driver.find_element(By.XPATH, BC.CONSTRUCTOR_HEADER)
        assert construct_burger.text == 'Соберите бургер'

    def test_sign_out(self, driver, random_user, registration):
        driver.get(url=REGISTRATION_URL)
        registration()

        driver.get(url=BASE_URL)
        driver.find_element(By.XPATH, BC.SIGN_IN_ACCOUNT_BUTTON).click()
        wait_element_is_visible(driver, locator=BC.SIGN_IN_H2_TEXT)

        driver.find_element(By.XPATH, BC.SIGN_IN_EMAIL).send_keys(random_user.random_email)
        driver.find_element(By.XPATH, BC.SIGN_IN_PASSWORD).send_keys(random_user.random_password)
        enter_button = driver.find_element(By.XPATH, BC.SIGN_IN_BUTTON)
        enter_button.click()
        wait_element_is_not_visible(driver, element=enter_button)

        link = driver.find_element(By.XPATH, BC.PERSONAL_ACCOUNT_LINK)
        driver.execute_script('arguments[0].click();', link)
        wait_element_is_present(driver, by=By.CSS_SELECTOR, locator='.input__textfield')

        driver.find_element(By.XPATH, BC.EXIT_BUTTON).click()
        h2 = wait_element_is_visible(driver, locator=BC.SIGN_IN_H2_TEXT)

        assert h2.text == "Вход"
