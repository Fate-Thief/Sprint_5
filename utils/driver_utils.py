from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class WaitForElementIsHidden:
    def __init__(self, by, search_condition, expected_value):
        self.__by = by
        self.__search_condition = search_condition
        self.__expected_value = expected_value

    def __call__(self, driver):
        rect = driver.find_element(self.__by, self.__search_condition).rect
        attribute_value = rect['y'] + rect['height'] > 0
        return attribute_value == self.__expected_value


def wait_element_is_visible(browser, locator: str, by: str = By.XPATH, timeout: int = 5, poll: float = 0.1):
    return WebDriverWait(browser, timeout=timeout, poll_frequency=poll).until(
        expected_conditions.visibility_of_element_located((by, locator))
    )


def wait_element_is_present(browser, locator: str, by: str = By.XPATH, timeout: int = 5, poll: float = 0.1):
    return WebDriverWait(browser, timeout=timeout, poll_frequency=poll).until(
        expected_conditions.presence_of_element_located((by, locator))
    )


def wait_element_is_not_visible(browser, element: tuple | WebElement, timeout: int = 5, poll: float = 0.1):
    return WebDriverWait(browser, timeout=timeout, poll_frequency=poll).until(
        expected_conditions.invisibility_of_element(element)
    )


def wait_element_is_clickable(browser, locator: str, by: str = By.XPATH, timeout: int = 5, poll: float = 0.1):
    return WebDriverWait(browser, timeout=timeout, poll_frequency=poll).until(
        expected_conditions.element_to_be_clickable((by, locator))
    )


def wait_element_is_hidden(
        browser, by: str, search_condition, expected_value: bool, timeout: int = 5, poll: float = 0.1
):
    return WebDriverWait(browser, timeout=timeout, poll_frequency=poll).until(
        WaitForElementIsHidden(by=by, search_condition=search_condition, expected_value=expected_value)
    )
