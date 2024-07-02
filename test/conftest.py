import pytest
from selenium import webdriver
from PersonalGenerator import PersonalGenerator
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from ByLocators import ByLocators as BC


@pytest.fixture(scope="class", params=['chrome'])
def setup(request):

    cred_generator = PersonalGenerator()
    request.cls.email = cred_generator.random_email
    request.cls.correct_password = cred_generator.random_password

    if request.param == "firefox":
        firefox_option = webdriver.FirefoxOptions()
        request.cls.driver_options = firefox_option
        driver = webdriver.Firefox(options=firefox_option)

    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("no-sandbox")
        chrome_options.add_argument("--headless")
        request.cls.driver_options = chrome_options
        driver = webdriver.Chrome(options=chrome_options)

    request.cls.driver = driver

    wait = Wait(driver, timeout = 5, poll_frequency = 0.1)
    request.cls.wait = wait

    yield driver
    driver.quit()


@pytest.fixture(scope="class", params=['chrome'])
def registration(request):
    request.cls.driver.get(url=request.cls.registration_url)
    request.cls.driver.maximize_window()
    request.cls.wait.until(expected.visibility_of_element_located((By.XPATH, BC.REGISTRATION_H2_TEXT)))

    # registration
    request.cls.driver.find_element(By.XPATH, BC.REGISTRATION_NAME_INPUT).send_keys(request.cls.user_name)
    request.cls.driver.find_element(By.XPATH, BC.REGISTRATION_EMAIL_INPUT).send_keys(request.cls.email)
    request.cls.driver.find_element(By.XPATH, BC.REGISTRATION_PASSWORD_INPUT).send_keys(request.cls.correct_password)
    request.cls.driver.find_element(By.XPATH, BC.REGISTRATION_BUTTON).click()


