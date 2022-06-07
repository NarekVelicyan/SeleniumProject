import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Locators import Locators
from Common.CustomFind import Find

class Delete_Product():
    def __init__(self, driver):
        self.driver = driver
        self.Locator = Locators.LocatorsClass
        self.Find = Find.FindElement(self.driver)


    def delete_one_product(self):
        deleteButton = self.Find.customFind(self.Locator.deleteLocator)
        deleteButton.click()

    def delete_all_products(self):
        CartItems = self.Find.customFind(self.Locator.CartNumber)
        CartItemsNumber = int(CartItems.text)
        for i in range (CartItemsNumber):
            self.delete_one_product()
            time.sleep(2)



