from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

PATH = "C:\Program Files (x86)\chromedriver.exe"

service = Service(PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://www.nhl.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)  

#click into stat page
statsElement = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Stats')]")))
statsElement.click()
driver.implicitly_wait(5)
#print("Stat Page")

#click into Skaters tab
statTab = driver.find_element(By.ID, "skaters").click()
#print("Skater tab")

now = datetime.datetime.now()

userTestSelect = 3
match userTestSelect:
    case 1:
        print("Top 5 Goal Leaders: ( As of", now , ")")
        for count in range(3):
            clickGoal = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Goals']")))
            clickGoal.click()
            #print("CLicked goal column")

        rows = driver.find_elements(By.XPATH, "//*[@id='season-tabpanel']/span/div/div[2]/table/tbody/tr")

        for i in range(min(5, len(rows))):
            nameAddress = rows[i].find_element(By.XPATH, "./td[2]/div/a")
            nameValue = nameAddress.text

            goalAddress = rows[i].find_element(By.XPATH, "./td[8]")
            goalValue = goalAddress.text
            print(nameValue + ":" , goalValue)

    case 2:
        print("Top 5 Assist Leaders: ( As of", now , ")")
        for count in range(3):
            clickAssist = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Assists']")))
            clickAssist.click()
            #print("CLicked assist column")

        rows = driver.find_elements(By.XPATH, "//*[@id='season-tabpanel']/span/div/div[2]/table/tbody/tr")

        for i in range(min(5, len(rows))):
            nameAddress = rows[i].find_element(By.XPATH, "./td[2]/div/a")
            nameValue = nameAddress.text

            assistAddress = rows[i].find_element(By.XPATH, "./td[9]")
            assistValue = assistAddress.text
            print(nameValue + ": " , assistValue)

    case 3:
        print("Top 5 Point Leaders: ( As of", now , ")")
        for count in range(3):
            clickPoints = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Points']")))
            clickPoints.click()
            #print("CLicked points column")

        rows = driver.find_elements(By.XPATH, "//*[@id='season-tabpanel']/span/div/div[2]/table/tbody/tr")

        for i in range(min(5, len(rows))):
            nameAddress = rows[i].find_element(By.XPATH, "./td[2]/div/a")
            nameValue = nameAddress.text

            pointsAddress = rows[i].find_element(By.XPATH, "./td[10]")
            pointsValue = pointsAddress.text
            print(nameValue + ": " , pointsValue)
    
    case _:
        print("Error please try using a valid number.")


driver.quit()