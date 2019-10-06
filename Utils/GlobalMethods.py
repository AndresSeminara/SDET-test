

class GlobalMethods:
    @staticmethod
    def close_pop_up(driver):
        try:
            driver.find_element_by_xpath("//*[@class='close-layer']").click()
        except Exception as e:
            pass
