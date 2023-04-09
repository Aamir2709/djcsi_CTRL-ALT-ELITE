from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Set up options for the Chrome driver
def get_flipkart(email):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option("debuggerAddress","localhost:8989")

    # Initialize the Chrome driver and navigate to Flipkart login page
    driver = webdriver.Chrome(executable_path="D:\codeshastra\chromedriver.exe",options=options)
    driver.get("https://www.flipkart.com/account/login")

    # Find the username and password fields and enter your credentials
    username = driver.find_element(By.XPATH,"//input[@class='_2IX_2- VJZDxU']")
    username.send_keys(email)
    sleep(2)

    button = driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")
    button.click()

    sleep(2)
    try:
        element = driver.find_element(By.XPATH,"//input[@class='_2IX_2- VJZDxU']")
        return("Account doen't exists")
    except NoSuchElementException:
        return("Account exists")
    # Submit the form

