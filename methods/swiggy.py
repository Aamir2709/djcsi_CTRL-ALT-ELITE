from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By


def get_swiggy(Mobile):
    opt=Options()
    opt.add_experimental_option("debuggerAddress","localhost:8989")
    driver= webdriver.Chrome(executable_path="D:\codeshastra\chromedriver.exe",options=opt)
    driver.get("https://www.swiggy.com/auth")
    input_elem = driver.find_element(By.ID,"mobile").send_keys(int(Mobile))
    # find the div containing the a tag using a CSS selector
    sleep(2)
    # find the a tag inside the div using a CSS selector
    button = driver.find_element(By.XPATH,"//button[@class='_1vTVI _2UPEv']")
    button.click()
    sleep(2)
    try:
        element = driver.find_element(By.ID,'name') # or use find_element_by_id()
        return("Account does not exist")
    except NoSuchElementException:
        return("Account exists")

