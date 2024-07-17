from selenium.webdriver.common.by import By

from consts.constants import BASE_URL
from locators.by_locators import ByLocators as BC
from utils.driver_utils import wait_element_is_hidden


class TestConstructor:
    def test_buns_tab_is_active_by_default(self, driver):
        driver.get(url=BASE_URL)
        driver.find_element(By.XPATH, BC.CONSTRUCTOR_HEADER)

        span = driver.find_element(By.XPATH, BC.CONSTRUCTOR_SAUCES_SPAN)
        assert span.text == 'Булки'

    def test_click_sauces_switch_to_sauces(self, driver):
        driver.get(url=BASE_URL)

        sauces = driver.find_element(By.XPATH, BC.CONSTRUCTOR_BUNS_DIV)
        driver.execute_script('arguments[0].click();', sauces)
        wait_element_is_hidden(driver, by=By.XPATH, search_condition=BC.CONSTRUCTOR_BUNS_H2_TEXT, expected_value=True)

        current_span = driver.find_element(By.XPATH, BC.CONSTRUCTOR_SAUCES_SPAN)
        assert current_span.text == 'Соусы'

    def test_click_dips_switch_to_dips(self, driver):
        driver.get(url=BASE_URL)

        dips = driver.find_element(By.XPATH, BC.CONSTRUCTOR_DIPS_DIV)
        driver.execute_script('arguments[0].click();', dips)
        wait_element_is_hidden(driver, by=By.XPATH, search_condition=BC.CONSTRUCTOR_SAUCES_H2_TEXT, expected_value=True)

        current_span = driver.find_element(By.XPATH, BC.CONSTRUCTOR_SAUCES_SPAN)
        assert current_span.text == 'Начинки'
