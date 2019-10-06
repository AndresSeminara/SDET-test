import unittest
from selenium import webdriver
from Config.Config import *
from Pages.HomePage import HomePage
from Pages.SearchResults import SearchResults
from Pages.ItemPage import ItemPage


class AliExpress(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(Browser['Chrome'])
        self.driver.get(Environments['Prod'])
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)
        self.search_results = SearchResults(self.driver)
        self.item_page = ItemPage(self.driver)

    def test_item_availability(self):
        assert 'AliExpress' in self.driver.title
        # TODO: CHANGE SEARCH VALUE TO AN ARGUMENT OR SOMETHING ELSE
        search_input = 'Iphone'
        self.home_page.search_item(search_input)

        # Scrolling to button Next
        self.search_results.go_to_next_page()
        self.search_results.click_on_item()
        item_quantity = self.item_page.get_product_quantity()
        assert item_quantity > 0, 'This item can\'t be bought.'

    def tearDown(self):
        self.driver.close()
