from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Locators import Locators
from Common.CustomFind import Find

class LoginSection():
    def __init__(self, driver):
        self.driver = driver
        self.Locators = Locators.LocatorsClass()
        self.Find = Find.FindElement(self.driver)


    def inpute_email_or_number(self, argument):
        self.emailSection = self.Find.customFind(self.Locators.emailSectionLocator)
        self.emailSection.click()
        self.emailSection.send_keys(argument)



    def press_to_continue_button(self):
        self.continueButton = self.Find.customFind(self.Locators.continueButtonLocator)
        self.continueButton.click()