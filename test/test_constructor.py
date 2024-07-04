import pytest
from selenium.webdriver.common.by import By
from ByLocators import ByLocators as BC


class WaitForElementIsHidden(object):
    def __init__(self, by, search_condition, expected_value):
        self.__by = by
        self.__search_condition = search_condition
        self.__expected_value = expected_value

    def __call__(self, driver):
        rect = driver.find_element(self.__by, self.__search_condition).rect
        attribute_value = rect['y'] + rect['height'] > 0
        return attribute_value == self.__expected_value


@pytest.mark.usefixtures("setup")
class TestConstructor:
    url = 'https://stellarburgers.nomoreparties.site/'

    def test_buns_tab_is_active_by_default(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, BC.CONSTRUCTOR_HEADER)

        span = self.driver.find_element(By.XPATH, BC.CONSTRUCTOR_SAUCES_SPAN)
        assert span.text == 'Булки'

    def test_click_sauces_switch_to_sauces(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sauces = self.driver.find_element(By.XPATH, BC.CONSTRUCTOR_BUNS_DIV)
        self.driver.execute_script('arguments[0].click();', sauces)
        self.wait.until(WaitForElementIsHidden(by=By.XPATH, search_condition=BC.CONSTRUCTOR_BUNS_H2_TEXT, expected_value=True))

        current_span = self.driver.find_element(By.XPATH, BC.CONSTRUCTOR_SAUCES_SPAN)
        assert current_span.text == 'Соусы'

    def test_click_dips_switch_to_dips(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        dips = self.driver.find_element(By.XPATH, BC.CONSTRUCTOR_DIPS_DIV)
        self.driver.execute_script('arguments[0].click();', dips)
        self.wait.until(WaitForElementIsHidden(by=By.XPATH, search_condition=BC.CONSTRUCTOR_SAUCES_H2_TEXT, expected_value=True))

        current_span = self.driver.find_element(By.XPATH, BC.CONSTRUCTOR_SAUCES_SPAN)
        assert current_span.text == 'Начинки'
