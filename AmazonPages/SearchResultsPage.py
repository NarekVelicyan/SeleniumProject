from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Locators import Locators
from Common.CustomFind import Find

class SearchResults():
    def __init__(self, driver):
        self.driver = driver
        self.Locator = Locators.LocatorsClass
        self.Find = Find.FindElement(self.driver)


    def select_any_product(self):
        selectProduct = self.Find.customFind(self.Locator.selectProductLocator)
        selectProduct.click()