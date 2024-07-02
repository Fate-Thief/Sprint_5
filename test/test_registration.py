import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from ByLocators import ByLocators as BC


@pytest.mark.usefixtures("setup")
class TestRegistration:
    url = 'https://stellarburgers.nomoreparties.site/'
    user_name = 'Nastia'
    incorrect_password = '123'

    def test_success_registration(self):
        self.driver.get(url=self.url)
        self.driver.maximize_window()

        self.driver.find_element(By.XPATH, BC.SIGN_IN_ACCOUNT_BUTTON).click()
        self.wait.until(expected.visibility_of_element_located((By.XPATH, BC.SIGN_IN_H2_TEXT)))

        self.driver.find_element(By.XPATH, BC.REGISTRATION_LINK).click()
        registration = self.wait.until(expected.visibility_of_element_located((By.XPATH, BC.REGISTRATION_H2_TEXT)))

        self.driver.find_element(By.XPATH, BC.REGISTRATION_NAME_INPUT).send_keys(self.user_name)
        self.driver.find_element(By.XPATH, BC.REGISTRATION_EMAIL_INPUT).send_keys(self.email)
        self.driver.find_element(By.XPATH, BC.REGISTRATION_PASSWORD_INPUT).send_keys(self.correct_password)
        self.driver.find_element(By.XPATH, BC.REGISTRATION_BUTTON).click()
        self.wait.until(expected.invisibility_of_element(registration))

        element = self.wait.until(expected.visibility_of_element_located((By.TAG_NAME, 'h2')))
        assert element.text == 'Вход'

    def test_registration_with_incorrect_password(self):
        self.driver.get(url=self.url)
        self.driver.maximize_window()

        self.driver.find_element(By.XPATH, BC.SIGN_IN_ACCOUNT_BUTTON).click()
        self.wait.until(expected.visibility_of_element_located((By.XPATH, BC.SIGN_IN_H2_TEXT)))

        self.driver.find_element(By.XPATH, BC.REGISTRATION_LINK).click()
        self.wait.until(expected.element_to_be_clickable((By.XPATH, BC.REGISTRATION_H2_TEXT)))

        self.driver.find_element(By.XPATH, BC.REGISTRATION_NAME_INPUT).send_keys(self.user_name)
        self.driver.find_element(By.XPATH, BC.REGISTRATION_EMAIL_INPUT).send_keys(self.email)
        self.driver.find_element(By.XPATH, BC.REGISTRATION_PASSWORD_INPUT).send_keys(self.incorrect_password)
        self.driver.find_element(By.XPATH, BC.REGISTRATION_BUTTON).click()

        element = self.wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, '.input__error')))
        assert element.text == 'Некорректный пароль'








