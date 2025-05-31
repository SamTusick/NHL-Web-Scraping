# driver.py
# Chrome Web Driver
# Sets up and return driver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

def get_driver():
    # Gets rid of certain error messages
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    PATH = "C:\Program Files (x86)\chromedriver-win64\chromedriver.exe"
    service = Service(PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)


    wait = WebDriverWait(driver, 10) 
    return driver, wait
