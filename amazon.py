from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

opt=Options()
opt.add_experimental_option("debuggerAddress","localhost:8989")


driver= webdriver.Chrome(executable_path="D:\codeshastra\chromedriver.exe",options=opt)
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&prevRID=FWHWVVMJNB34WM2N9QVS&openid.assoc_handle=usflex&openid.mode=checkid_setup&failedSignInCount=0&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
input_elem = driver.find_element(By.ID,"ap_email").clear()
input_elem = driver.find_element(By.ID,"ap_email").send_keys("aamirbaugwala@gmail.com")

button_elem = driver.find_element_by_id("continue")
button_elem.click()




sleep(3)
try:
    if driver.find_element_by_id("auth-create-account-link"):
        print("NO Account")
except:
    print("Account found")
