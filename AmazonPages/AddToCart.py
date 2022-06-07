from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Locators import Locators
from Common.CustomFind import Find

class Add():
    def __init__(self, driver):
        self.driver = driver
        self.Locator = Locators.LocatorsClass
        self.Find = Find.FindElement(self.driver)


    def add_to_cart(self):
        addToCart = self.Find.customFind(self.Locator.addToCartLocator)
        addToCart.click()