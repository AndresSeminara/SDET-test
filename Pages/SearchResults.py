from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Utils.GlobalMethods import GlobalMethods
from selenium.webdriver.common.action_chains import ActionChains
import time


class SearchResults:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.item = (By.XPATH, '//div[@product-index="1"]//a[@class="item-title"]')
        self.btn_next = (By.XPATH, '//button[@aria-label="Next page, current page 1"]')

    def get_item(self, item_position):
        item_list = self.driver.find_elements(*self.item)
        return item_list[item_position]

    def click_on_item(self):
        self.driver.implicitly_wait(1)
        GlobalMethods.close_pop_up(self.driver)
        ActionChains(self.driver).move_to_element(self.driver.find_element(*self.item)).click().perform()

        for x in range(0, 20):
            try:
                self.driver.switch_to.window(self.driver.window_handles[1])
            except:
                time.sleep(0.5)

    def go_to_next_page(self):
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.END)

        for counter in range(0, 49):
            flag = False
            GlobalMethods.close_pop_up(self.driver)

            try:
                self.driver.find_element(*self.btn_next)
                flag = True
            except:
                self.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)
            if flag is True:
                break

        ActionChains(self.driver).move_to_element(self.driver.find_element(*self.btn_next)).click().perform()
