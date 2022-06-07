from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Locators import Locators
from Common.CustomFind import Find

class EditName():
    def __init__(self, driver):
        self.driver = driver
        self.Locator = Locators.LocatorsClass
        self.Find = Find.FindElement(self.driver)


    def inpute_name(self, argument):
        InputeNameSection = self.Find.customFind(self.Locator.EditName)
        InputeNameSection.click()
        InputeNameSection.clear()
        InputeNameSection.send_keys(argument)

    def press_to_SaveChanges_Button(self):
        SaveChanges = self.Find.customFind(self.Locator.SaveChanges)
        SaveChanges.click()

