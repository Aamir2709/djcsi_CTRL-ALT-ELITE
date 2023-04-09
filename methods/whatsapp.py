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
driver = webdriver.Chrome(executable_path='D:\codeshastra\chromedriver.exe', options=opt)

wait = WebDriverWait(driver, 10)


def get_whatsapp(phoneNumber):

    # Open the URL
    url = "https://wa.me/+91" + phoneNumber 
    driver.get(url)
    l = []

    # Wait for the button to load
    # button = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Continue to Chat')]"))
    # )

    button = driver.find_element_by_id("action-button")

    # Click the button
    button.click()

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    if driver.current_url=="https://api.whatsapp.com/send/?phone=%2B91{phone}&text&type=phone_number&app_absent=0".format(phone=phoneNumber):
        #print("hello")

        buttons = driver.find_elements(By.XPATH, "//a[@class='_9vcv _9vcx']")
        # print(buttons.text)
        count = 0
        for button in buttons:
            if count==0:
                count+=1
            else:
                #print(button.get_attribute("href"))
                driver.get(button.get_attribute("href"))
                

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    driver.implicitly_wait(10)
    try:
        element2 = driver.find_element(By.XPATH, "//*[contains(text(), 'Phone number shared via url is invalid.')]")
        #print(element2.text)
        l.append("number does not exist")
        
        #Phone number shared via url is invalid.
    except:
        l.append("number exists")

    # driver.find_element(By.XPATH, "//div[@role='button']").click()

    driver.find_element(By.XPATH, "//header[@class='_23P3O']").click()

    try:
        imageDiv = driver.find_elements(By.XPATH, "//div[@role='button' and @class='g0rxnol2 g9p5wyxn i0tg5vk9 aoogvgrq o2zu3hjb']/img")
        # image = imageDiv.find_element(By.XPATH, "//div/img").get_attribute("src")
        l.append(imageDiv[1].get_attribute("src"))
    except:
        l.append("no image")
    
    return l


    # Close the webdriver
    driver.quit()   