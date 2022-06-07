from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Locators import Locators
from Common.CustomFind import Find
from selenium.webdriver.common.action_chains import ActionChains

class MainPage():
    def __init__(self, driver):
        self.driver = driver
        self.Locator = Locators.LocatorsClass
        self.Find = Find.FindElement(self.driver)

    def Search_Field(self, argument):
        searchField = self.Find.customFind(self.Locator.searchFieldLocator)
        searchField.click()
        searchField.send_keys(argument)
        searchField.send_keys(Keys.ESCAPE)

    def press_to_search_button(self):
        searchFieldProduct = self.Find.customFind(self.Locator.searchButtonLocator)
        searchFieldProduct.click()

    def press_Cart_Button(self):
        CartButton = self.Find.customFind(self.Locator.cartPageLocator)
        CartButton.click()

    def press_to_account_button(self):
        AccountButton = self.Find.customFind(self.Locator.AccountButtonLocator)
        AccountButton.click()

    def move_to_account_button(self):
        MoveToButton = self.Find.customFind(self.Locator.AccountButtonLocator)
        action = ActionChains(self.driver)
        action.move_to_element(MoveToButton).perform()

    def press_to_signout_button(self):
        SignOuteSection = self.Find.customFind(self.Locator.SignOut)
        SignOuteSection.click()


