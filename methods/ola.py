from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Set up options for the Chrome driver
def get_ola(number):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option("debuggerAddress","localhost:8989")

    # Initialize the Chrome driver and navigate to Flipkart login page
    driver = webdriver.Chrome(executable_path="D:\codeshastra\chromedriver.exe",options=options)
    driver.get("https://accounts.olacabs.com/?returnurl=https%3A%2F%2Fhelp.olacabs.com%2Fsupport%2Fmain&utm_source=ola_care_login")
    sleep(4)
    button1 = driver.find_element(By.ID,"phone-number").send_keys(number)
    sleep(4)
    try:
        button = driver.find_element(By.ID,"recaptcha-anchor")
        button.click()
        sleep(2)
    except:
        pass

    button = driver.find_element(By.XPATH,"//div[@class='sso__cta enabled']")
    button.click()
    sleep(2)

    # try:
    #     button = driver.find_element(By.ID,"recaptcha-anchor")
    #     button.click()
    #     sleep(2)
    # except:
    #     pass


    try:

        element = driver.find_element(By.ID,"otp")
        return("Yes")
    except NoSuchElementException:
        return("No")
    # Submit the form



