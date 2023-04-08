from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


# Initialize the webdriver
# driver = webdriver.Chrome()
opt=Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
# opt.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='C:/Users/akash/Downloads/chromedriver_win32_111/chromedriver.exe', options=opt)

wait = WebDriverWait(driver, 10)


def revvScript(email):

    # Open the URL
    url = "https://www.revv.co.in"
    driver.get(url)

    link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login or Signup")))

    # Click on the link
    link.click()

    wait.until(EC.element_to_be_clickable((By.NAME, 'email'))).send_keys(email)  

    # email_input = driver.find_element(By.xpath("//input[@placeholder='Enter your email']"))
    # email_input.click()
    # email_input.send_keys(email)
    driver.implicitly_wait(10)

    # Find the login button and click on it
    login_button = driver.find_element(By.XPATH, "//button[@class='btn login-proceed ']")
    login_button.click()

    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='error-title']")))
        print("Email does not exist")
    except:
        print("Email exists")

    
    driver.quit()   

revvScript("example@gmail.com")