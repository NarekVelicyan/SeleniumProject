import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
from AmazonPages import EmailSectionPage
from AmazonPages import PasswordSectionPage
from AmazonPages import AmazonMainPage
from AmazonPages import SearchResultsPage
from AmazonPages import AddToCart
from Common.Variables import Variables
from AmazonPages import CartPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class AmazonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        cls.EmailPage = EmailSectionPage.LoginSection(cls.driver)
        cls.PasswordSectionPage = PasswordSectionPage.PasswordSection(cls.driver)
        cls.AmazonMainPage = AmazonMainPage.MainPage(cls.driver)
        cls.SearchResults = SearchResultsPage.SearchResults(cls.driver)
        cls.AddToCart = AddToCart.Add(cls.driver)
        cls.DeleteFromCart = CartPage.Delete_Product(cls.driver)
        cls.Variables = Variables.ProjectVariables()
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get(self.Variables.mainURL)


    def test_DeleteTest(self):
        self.EmailPage.inpute_email_or_number("velicyan.narek@bk.ru")
        self.EmailPage.press_to_continue_button()
        self.PasswordSectionPage.inpute_password("159753asdfvbnm")
        self.PasswordSectionPage.press_to_remember_box()
        self.PasswordSectionPage.press_to_sumbit()
        self.AmazonMainPage.press_Cart_Button()
        self.DeleteFromCart.delete_all_products()


    def tearDown(self):
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()