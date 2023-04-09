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
driver.get("https://www.zomato.com/")
# input_elem = driver.find_element(By.ID,"ap_email").clear()
# input_elem = driver.find_element(By.ID,"ap_email").send_keys("aamirbaugwala@gmail.com")

# button_elem = driver.find_element_by_tag_name("sc-3o0n99-5 sc-SFOxd hGFUqG")
# button_elem.click()


li_tags = driver.find_elements_by_tag_name("li")

# find all the a tags inside each li tag
for li_tag in li_tags:
    
        print(li_tag.get_attribute("class")=='sc-3o0n99-4 kAUthO')


