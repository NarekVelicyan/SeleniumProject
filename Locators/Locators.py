from selenium.webdriver.common.by import By

class LocatorsClass():
    #emailSection Locators
    emailSectionLocator = (By.ID, "ap_email")
    continueButtonLocator = (By.ID, "continue")

    #passwordSection Locators
    passwordSectionLocator = (By.ID, "ap_password")
    rememberBoxLocator = (By.XPATH, "//input[@name='rememberMe']")
    sumbitButtonLocator = (By.ID, "signInSubmit")

    #searchSection Locators
    searchFieldLocator = (By.ID, "twotabsearchtextbox")
    searchButtonLocator = (By.ID, "nav-search-submit-button")


    #selectProductSection Locator
    selectProductLocator = (By.XPATH, "(//img[@class='s-image'])[2]")

    #addToCartSection Locator
    addToCartLocator = (By.ID, "add-to-cart-button")

    #cartPage Locator
    cartPageLocator = (By.ID, "nav-cart-count-container")
    deleteLocator = (By.XPATH, "//input[@value='Delete']")

    #accountPage Locator
    AccountButtonLocator = (By.ID, "nav-link-accountList-nav-line-1")

    #yourProfileSection Locator
    yourProfileSection = (By.XPATH, "//img[@alt='Your Profiles']")

    #ManageYourProfiles Locator
    ManageYourProfile = (By.XPATH, "//div[@class='a-column a-span12']")

    #AccountNamePen Locator
    AccountNamePen = (By.ID, "name-edit-modal-link")

    #EditName Locator
    EditName = (By.ID, "profile-name-text-input")
    SaveChanges = (By.ID, "profile-name-edit-submit-button")

    #SignOut Locator
    SignOut = (By.ID, "nav-item-signout")

    #CartNumber Locator
    CartNumber = (By.ID, "nav-cart-count")