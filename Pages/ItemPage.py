from selenium.webdriver.common.by import By
import re


class ItemPage:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.product_quantity = (By.XPATH, '//div[@class="product-quantity-tip"]/span')

    def get_product_quantity(self):
        product_quantity = self.driver.find_element(*self.product_quantity).text
        return int(re.sub('[^0-9]', "", product_quantity))
