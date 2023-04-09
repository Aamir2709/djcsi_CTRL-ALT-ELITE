from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

def get_facebook(email):
    opt=Options()
    opt.add_experimental_option("debuggerAddress","localhost:8989")

    driver= webdriver.Chrome(executable_path="D:\codeshastra\chromedriver.exe",options=opt)
    driver.get("https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0")
    input_elem = driver.find_element(By.ID,"identify_email").clear()
    input_elem = driver.find_element(By.ID,"identify_email").send_keys(email)

    button_elem = driver.find_element_by_id("did_submit")
    button_elem.click()




    sleep(3)
    # Get the URL of the page after submitting the form
    next_url = driver.current_url
    if next_url=="https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0":
        return("Account doesn't exists")
    else:
        return("Account Exists")

