import time
import names
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
from AmazonPages import EmailSectionPage
from AmazonPages import PasswordSectionPage
from AmazonPages import AmazonMainPage
from AmazonPages import YourAccountPage
from AmazonPages import ManageYourProfilesPage
from AmazonPages import PersonalDetailsPage
from AmazonPages import EditNamePage
from Common.Variables import Variables
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class AmazonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        cls.EmailPage = EmailSectionPage.LoginSection(cls.driver)
        cls.PasswordSectionPage = PasswordSectionPage.PasswordSection(cls.driver)
        cls.Variables = Variables.ProjectVariables()
        cls.AmazonMainPage = AmazonMainPage.MainPage(cls.driver)
        cls.ManageYourAccount = ManageYourProfilesPage.YourAccount(cls.driver)
        cls.YourAccountPage = YourAccountPage.YourAccount(cls.driver)
        cls.PersonalDetails = PersonalDetailsPage.PersonalDetails(cls.driver)
        cls.EditeName = EditNamePage.EditName(cls.driver)
        cls.driver.maximize_window()


    def setUp(self):
        self.driver.get(self.Variables.mainURL)


    def test_SignIn(self):
        self.EmailPage.inpute_email_or_number("velicyan.narek@bk.ru")
        self.EmailPage.press_to_continue_button()
        self.PasswordSectionPage.inpute_password("159753asdfvbnm")
        self.PasswordSectionPage.press_to_remember_box()
        self.PasswordSectionPage.press_to_sumbit()
        self.AmazonMainPage.press_to_account_button()
        self.YourAccountPage.press_to_yourProfile_Section()
        self.ManageYourAccount.press_to_manage_yourProfile_Section()
        self.PersonalDetails.press_to_accountname_pen_button()
        self.EditeName.inpute_name(names.get_full_name(gender= 'male'))
        self.EditeName.press_to_SaveChanges_Button()

    def tearDown(self):
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()