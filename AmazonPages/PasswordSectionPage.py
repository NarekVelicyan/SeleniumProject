from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Locators import Locators
from Common.CustomFind import Find


class PasswordSection():
    def __init__(self, driver):
        self.driver = driver
        self.Locators = Locators.LocatorsClass
        self.Find = Find.FindElement(self.driver)

    def inpute_password(self, argument):
        passwordSection = self.Find.customFind(self.Locators.passwordSectionLocator)
        passwordSection.click()
        passwordSection.send_keys(argument)

    def press_to_remember_box(self):
        rememberBoxSection = self.Find.customFind(self.Locators.rememberBoxLocator)
        rememberBoxSection.click()

    def press_to_sumbit(self):
        signinSection = self.Find.customFind(self.Locators.sumbitButtonLocator)
        signinSection.click()
