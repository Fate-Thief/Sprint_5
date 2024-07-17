import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from locators.by_locators import ByLocators as BC
from utils.driver_utils import wait_element_is_visible

from utils.personal_generator import PersonalGenerator


@pytest.fixture()
def random_user() -> PersonalGenerator:
    return PersonalGenerator()


@pytest.fixture(params=['chrome'])
def driver(request):
    if request.param == "firefox":
        firefox_option = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_option)
    elif request.param == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        raise ValueError("Please select correct browser type")

    yield driver
    driver.quit()


@pytest.fixture()
def registration(driver, random_user):
    def _register():
        wait_element_is_visible(driver, locator=BC.REGISTRATION_H2_TEXT)

        # registration
        driver.find_element(By.XPATH, BC.REGISTRATION_NAME_INPUT).send_keys(random_user.username)
        driver.find_element(By.XPATH, BC.REGISTRATION_EMAIL_INPUT).send_keys(random_user.random_email)
        driver.find_element(By.XPATH, BC.REGISTRATION_PASSWORD_INPUT).send_keys(random_user.random_password)
        driver.find_element(By.XPATH, BC.REGISTRATION_BUTTON).click()

    yield _register

# @pytest.fixture()
# def login(driver, random_user):
#     def _login():
#         wait_element_is_visible(driver, locator=BC.SIGN_IN_H2_TEXT)
#
#         driver.find_element(By.XPATH, BC.SIGN_IN_EMAIL).send_keys(random_user.random_email)
#         driver.find_element(By.XPATH, BC.SIGN_IN_PASSWORD).send_keys(random_user.random_password)
#         enter_button = driver.find_element(By.XPATH, BC.SIGN_IN_BUTTON)
#         enter_button.click()
#         wait_element_is_not_visible(driver, element=enter_button)
#     yield _login
