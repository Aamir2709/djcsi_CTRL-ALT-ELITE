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


def whatsappScript(phoneNumber):

    # Open the URL
    url = "https://wa.me/+91" + phoneNumber 
    driver.get(url)

    # Wait for the button to load
    # button = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Continue to Chat')]"))
    # )

    button = driver.find_element_by_id("action-button")

    # Click the button
    button.click()

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    if driver.current_url=="https://api.whatsapp.com/send/?phone=%2B91{phone}&text&type=phone_number&app_absent=0".format(phone=phoneNumber):
        print("hello")
        # urlstring = 'https://web.whatsapp.com/send/?phone=%2B91{phone}&text&type=phone_number&app_absent=0'.format(phone=phoneNumber)
        # button2 = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "a._9vcv._9vcx[href={url}]".format(url=urlstring)))
        # )
        # Click the button
        # button2.click()
        # buttons = WebDriverWait(driver, 10).until(
        #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a._9vcv._9vcx"))
        # )
        buttons = driver.find_elements(By.XPATH, "//a[@class='_9vcv _9vcx']")
        # print(buttons.text)
        count = 0
        for button in buttons:
            if count==0:
                count+=1
            else:
                print(button.get_attribute("href"))
                driver.get(button.get_attribute("href"))
                

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # # Wait for the anchor tag to load
    # button3 = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//a[span[contains(text(), 'Use WhatsApp Web')]]"))
    # )

    # # Click the button
    # button3.click()
    # wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # element = driver.find_element(By.CSS_SELECTOR, "[data-testid='popup-contents']")
    driver.implicitly_wait(10)
    try:
        element2 = driver.find_element(By.XPATH, "//*[contains(text(), 'Phone number shared via url is invalid.')]")
        print(element2.text)
        print("number does not exist")
        return
        #Phone number shared via url is invalid.
    except:
        print("number exists")

    driver.find_element(By.XPATH, "//div[@role='button']").click()

    
     

    # print(element2.text)
    # print(element.text)

    # Close the webdriver
    driver.quit()   

# whatsappScript("8830051111")
whatsappScript("7093108528")