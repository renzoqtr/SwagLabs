from selenium.webdriver.common.by import By


class ProductsPage:
    PRODUCT_NAME = By.CSS_SELECTOR, "[data-test='inventory-item-name']"

    def __init__(self, driver):
        self.driver = driver

    def get_title_elements(self):
        title_elements = self.driver.find_elements(*self.PRODUCT_NAME)
        titles = []
        for element in title_elements:
            titles.append(element.text)
        return titles
