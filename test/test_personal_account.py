import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from ByLocators import ByLocators as BC


@pytest.mark.usefixtures("setup", "registration")
class TestPersonalAccount:
    url = 'https://stellarburgers.nomoreparties.site/'
    registration_url = 'https://stellarburgers.nomoreparties.site/register'
    user_name = 'Nastia'

    @pytest.fixture(scope='function', autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome(options=self.driver_options)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)

        yield self.driver
        self.driver.quit()

    def test_go_to_personal_account_authorized_user(self):
        self.driver.find_element(By.XPATH, BC.SIGN_IN_ACCOUNT_BUTTON).click()
        self.wait.until(expected.visibility_of_element_located((By.XPATH, BC.SIGN_IN_H2_TEXT)))

        self.driver.find_element(By.XPATH, BC.SIGN_IN_EMAIL).send_keys(self.email)
        self.driver.find_element(By.XPATH, BC.SIGN_IN_PASSWORD).send_keys(self.correct_password)
        enter_button = self.driver.find_element(By.XPATH, BC.SIGN_IN_BUTTON)
        enter_button.click()
        self.wait.until(expected.invisibility_of_element(enter_button))

        account_link = self.driver.find_element(By.XPATH, BC.PROFILE_LINK)
        self.driver.execute_script('arguments[0].click();', account_link)

        self.wait.until(expected.presence_of_element_located((By.CSS_SELECTOR, '.input__textfield')))
        account = self.driver.find_elements(By.CSS_SELECTOR, '.input__textfield')[0]

        assert account.get_property('value') == self.user_name

    def test_go_from_personal_account_to_constructor_clicking_by_logo(self):
        self.driver.find_element(By.XPATH, BC.SIGN_IN_ACCOUNT_BUTTON).click()
        self.wait.until(expected.visibility_of_element_located((By.XPATH, BC.SIGN_IN_H2_TEXT)))

        self.driver.find_element(By.XPATH, BC.SIGN_IN_EMAIL).send_keys(self.email)
        self.driver.find_element(By.XPATH, BC.SIGN_IN_PASSWORD).send_keys(self.correct_password)
        enter_button = self.driver.find_element(By.XPATH, BC.SIGN_IN_BUTTON)
        enter_button.click()
        self.wait.until(expected.invisibility_of_element(enter_button))

        link = self.driver.find_element(By.XPATH, BC.PERSONAL_ACCOUNT_LINK)
        self.driver.execute_script('arguments[0].click();', link)
        self.wait.until(expected.presence_of_element_located((By.CSS_SELECTOR, '.input__textfield')))

        self.driver.find_element(By.XPATH, BC.LOGO_BUTTON_LINK).click()
        construct_burger = self.driver.find_element(By.XPATH, BC.CONSTRUCTOR_HEADER)
        assert construct_burger.text == 'Соберите бургер'

    def test_sign_out(self):
        self.driver.find_element(By.XPATH, BC.SIGN_IN_ACCOUNT_BUTTON).click()
        self.wait.until(expected.visibility_of_element_located((By.XPATH, BC.SIGN_IN_H2_TEXT)))

        self.driver.find_element(By.XPATH, BC.SIGN_IN_EMAIL).send_keys(self.email)
        self.driver.find_element(By.XPATH, BC.SIGN_IN_PASSWORD).send_keys(self.correct_password)
        enter_button = self.driver.find_element(By.XPATH, BC.SIGN_IN_BUTTON)
        enter_button.click()
        self.wait.until(expected.invisibility_of_element(enter_button))

        link = self.driver.find_element(By.XPATH, BC.PERSONAL_ACCOUNT_LINK)
        self.driver.execute_script('arguments[0].click();', link)
        self.wait.until(expected.presence_of_element_located((By.CSS_SELECTOR, '.input__textfield')))

        self.driver.find_element(By.XPATH, BC.EXIT_BUTTON).click()
        h2 = self.wait.until(expected.visibility_of_element_located((By.XPATH, BC.SIGN_IN_H2_TEXT)))

        assert h2.text == "Вход"
