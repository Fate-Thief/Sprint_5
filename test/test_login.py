import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from ByLocators import ByLocators as BC


@pytest.mark.usefixtures("setup", "registration")
class TestAccountAccess:

    url = 'https://stellarburgers.nomoreparties.site/'
    registration_url = 'https://stellarburgers.nomoreparties.site/register'
    user_name = 'Nastia'

    @pytest.fixture(scope='function', autouse=True)
    def setup_and_teardown(self):

        # get new browser for each test
        self.driver = webdriver.Chrome(options=self.driver_options)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

        yield self.driver
        self.driver.quit()

    def test_access_to_account_click_sign_in_button(self):

        self.driver.find_element(By.XPATH, BC.SIGN_IN_ACCOUNT_BUTTON).click()
        self.wait.until(expected.visibility_of_element_located((By.XPATH, BC.SIGN_IN_H2_TEXT)))

        self.driver.find_element(By.XPATH, BC.SIGN_IN_EMAIL).send_keys(self.email)
        self.driver.find_element(By.XPATH, BC.SIGN_IN_PASSWORD).send_keys(self.correct_password)
        enter_button = self.driver.find_element(By.XPATH, BC.SIGN_IN_BUTTON)
        enter_button.click()
        self.wait.until(expected.invisibility_of_element(enter_button))

        order_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
        assert order_button.text == 'Оформить заказ'

    def test_access_to_account_press_personal_account_link(self):

        link = self.driver.find_element(By.XPATH, BC.PERSONAL_ACCOUNT_LINK)
        self.driver.execute_script('arguments[0].click();', link)
        self.wait.until(expected.visibility_of_element_located((By.XPATH, BC.SIGN_IN_H2_TEXT)))

        self.driver.find_element(By.XPATH, BC.SIGN_IN_EMAIL).send_keys(self.email)
        self.driver.find_element(By.XPATH, BC.SIGN_IN_PASSWORD).send_keys(self.correct_password)
        enter_button = self.driver.find_element(By.XPATH, BC.SIGN_IN_BUTTON)
        enter_button.click()
        self.wait.until(expected.invisibility_of_element(enter_button))

        order_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
        assert order_button.text == 'Оформить заказ'

    def test_access_to_account_using_registration_link(self):

        self.driver.find_element(By.XPATH, BC.SIGN_IN_ACCOUNT_BUTTON).click()
        self.wait.until(expected.visibility_of_element_located((By.XPATH, BC.SIGN_IN_H2_TEXT)))

        self.driver.find_element(By.XPATH, BC.REGISTRATION_LINK).click()

        self.wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, '.undefined')))

        enter_link = self.driver.find_element(By.XPATH, BC.SIGN_IN_LINK)
        self.driver.execute_script('arguments[0].click();', enter_link)
        self.wait.until(expected.visibility_of_element_located((By.XPATH, BC.SIGN_IN_H2_TEXT)))

        self.driver.find_element(By.XPATH, BC.SIGN_IN_EMAIL).send_keys(self.email)
        self.driver.find_element(By.XPATH, BC.SIGN_IN_PASSWORD).send_keys(self.correct_password)
        enter_button = self.driver.find_element(By.XPATH, BC.SIGN_IN_BUTTON)
        enter_button.click()
        self.wait.until(expected.invisibility_of_element(enter_button))

        order_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
        assert order_button.text == 'Оформить заказ'

    def test_access_to_account_using_restore_password_link(self):

        self.driver.find_element(By.XPATH, BC.SIGN_IN_ACCOUNT_BUTTON).click()
        self.wait.until(expected.visibility_of_element_located((By.XPATH, BC.SIGN_IN_H2_TEXT)))

        self.driver.find_element(By.XPATH, BC.RESTORE_PASSWORD_LINK).click()
        self.wait.until(expected.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/h2')))

        enter_link = self.driver.find_element(By.XPATH, BC.SIGN_IN_LINK)
        self.driver.execute_script('arguments[0].click();', enter_link)

        self.wait.until(expected.visibility_of_element_located((By.XPATH, BC.SIGN_IN_H2_TEXT)))

        self.driver.find_element(By.XPATH, BC.SIGN_IN_EMAIL).send_keys(self.email)
        self.driver.find_element(By.XPATH, BC.SIGN_IN_PASSWORD).send_keys(self.correct_password)
        enter_button = self.driver.find_element(By.XPATH, BC.SIGN_IN_BUTTON)
        enter_button.click()
        self.wait.until(expected.invisibility_of_element(enter_button))

        order_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
        assert order_button.text == 'Оформить заказ'

















