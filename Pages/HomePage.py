from selenium.webdriver.common.by import By
from Utils.GlobalMethods import GlobalMethods


class HomePage:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.search_box = (By.XPATH, '//input[@name="SearchText"]')
        self.search_button = (By.XPATH, '//input[@type="submit" and @class="search-button"]')

    def search_item(self, item):
        self.driver.find_element(*self.search_box).send_keys(item)
        GlobalMethods.close_pop_up(self.driver)
        self.driver.find_element(*self.search_button).click()
