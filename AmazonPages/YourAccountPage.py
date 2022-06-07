from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Locators import Locators
from Common.CustomFind import Find

class YourAccount():
    def __init__(self, driver):
        self.driver = driver
        self.Locator = Locators.LocatorsClass
        self.Find = Find.FindElement(self.driver)


    def press_to_yourProfile_Section(self):
        yourProfileSection = self.Find.customFind(self.Locator.yourProfileSection)
        yourProfileSection.click()