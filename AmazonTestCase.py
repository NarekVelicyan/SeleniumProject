import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome("chromedriver.exe")
driver.delete_all_cookies()
driver.maximize_window()
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Fhomepage.html%2Fref%3Dsxts_snpl_5_0_f0446b5a-8dcd-4647-99b3-62ccafe61438%2F%3Fie%3DUTF8%26pd_rd_r%3D2fbf530f-782d-4666-a44e-dd554508a799%26pd_rd_w%3DEYbJB%26pd_rd_wg%3DfJlJW%26pf_rd_p%3Df0446b5a-8dcd-4647-99b3-62ccafe61438%26pf_rd_r%3DBK01T7NPRD2ZNY1TN1CN%26qid%3D1652511180%26ref_%3Dnav_em_hd_re_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&&ref_%3Dnav_em_hd_clc_signin')

emailSection = driver.find_element(By.ID, "ap_email")
emailSection.click()
emailSection.send_keys("velicyannarek@gmail.com")
continueButton = driver.find_element(By.ID, "continue")
continueButton.click()
passwordSection = driver.find_element(By.ID, "ap_password")
passwordSection.click()
passwordSection.send_keys("Tat16zxcvbnm")
rememberBoxSection = driver.find_element(By.XPATH, "//input[@name='rememberMe']")
rememberBoxSection.click()
signinSection = driver.find_element(By.ID, "signInSubmit")
signinSection.click()
AccountSection = driver.find_element(By.XPATH, "//span[@class='nav-line-2']")
AccountSectionSignOut = driver.find_element(By.ID, "nav-item-signout")
AccountSectionSignOut.click()

