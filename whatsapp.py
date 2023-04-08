import os
import pickle

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# you can set the chromedriver path on the system path and remove this variable
CHROMEDRIVER_PATH = ''
global SCROLL_TO, SCROLL_SIZE


def get_messages(driver, contact_list):
    global SCROLL_SIZE
    print('>>> getting messages')
    conversations = []
    for contact in contact_list:

        sleep(2)
        user = driver.find_element_by_xpath('//span[contains(@title, "{}")]'.format(contact))
        user.click()
        sleep(3)
        conversation_pane = driver.find_element_by_xpath("//div[@class='_2-aNW']")

        messages = set()
        length = 0
        scroll = SCROLL_SIZE
        while True:
            elements = driver.find_elements_by_xpath("//div[@class='copyable-text']")
            for e in elements:
                messages.add(e.get_attribute('data-pre-plain-text') + e.text)
            if length == len(messages):
                break
            else:
                length = len(messages)
            driver.execute_script('arguments[0].scrollTop = -' + str(scroll), conversation_pane)
            sleep(2)
            scroll += SCROLL_SIZE
        conversations.append(messages)
        filename = 'collected_data/conversations/{}.json'.format(contact)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'wb') as fp:
            pickle.dump(messages, fp)
    return conversations


def main():
    phoneNumber = "1234567890"
    global SCROLL_TO, SCROLL_SIZE
    SCROLL_SIZE = 600
    SCROLL_TO = 600
    contacts = []

    options = Options()
    options.add_argument('user-data-dir=./User_Data')  # saving user data so you don't have to scan the QR Code again
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://api.whatsapp.com/send/?phone=%2B911234567890&text&type=phone_number&app_absent=0")
    button = driver.find_element_by_id("action-button")
    # Click the button
    button.click()
    sleep(2)

if __name__ == "_main_":
    main()