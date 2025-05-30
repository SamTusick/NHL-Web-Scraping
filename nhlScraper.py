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
import time
import datetime
from userMenu import getUserSelection

#gets rid of certain error messages
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--headless")

def getUserInput():
    chosenStat = getUserSelection()
    print("\nRecieved input successfully: ", chosenStat)
    return chosenStat

PATH = "C:\Program Files (x86)\chromedriver-win64\chromedriver.exe"

service = Service(PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.nhl.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)  

def closeCookieWindow():
    try:
        #checks to see if cookie banner is present
        cookieAccept = driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']")
        cookieAccept.click()
        print("\nCookie window close successfully!\n")

    except Exception as e:
        print("\nError finding or closing cookie banner: " , e, "\n")     

closeCookieWindow()

#click into stat page
statsElement = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Stats')]")))
statsElement.click()
driver.implicitly_wait(5)
#print("Stat Page")

#click into Skaters tab
statTab = driver.find_element(By.ID, "skaters").click()
#print("Skater tab")

now = datetime.datetime.now()
#userLoop = 3

prevChosenStat = None
firstTime = True

while True:
    newChosenStat = getUserInput()

    if(firstTime):
        userLoop = 3
        firstTime = False
    elif(newChosenStat == prevChosenStat):
        userLoop = 0
    else:
        userLoop = 1

    prevChosenStat = newChosenStat

    match newChosenStat:
        case 1:
            print("\nTop 5 Goal Leaders: ( As of", now , ")")
            for count in range(userLoop):
                clickGoal = driver.find_element(By.XPATH, "//div[@title='Goals']")
        
                scroll_orgin = ScrollOrigin.from_element(clickGoal)
                ActionChains(driver)\
                    .scroll_to_element(clickGoal)\
                    .scroll_from_origin(scroll_orgin, 0, 200)\
                    .perform()
                time.sleep(0.5)
                
                clickGoal.click()
                #print("Clicked goal column")

            rows = driver.find_elements(By.XPATH, "//*[@id='season-tabpanel']/span/div/div[2]/table/tbody/tr")

            for i in range(min(5, len(rows))):
                nameAddress = rows[i].find_element(By.XPATH, "./td[2]/div/a")
                nameValue = nameAddress.text

                goalAddress = rows[i].find_element(By.XPATH, "./td[8]")
                goalValue = goalAddress.text
                print(nameValue + ":" , goalValue)

        case 2:
            print("\nTop 5 Assist Leaders: ( As of", now , ")")
            for count in range(userLoop):
                clickAssist = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Assists']")))

                scroll_orgin = ScrollOrigin.from_element(clickAssist)
                ActionChains(driver)\
                    .scroll_to_element(clickAssist)\
                    .scroll_from_origin(scroll_orgin, 0, 200)\
                    .perform()
                time.sleep(0.5)

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
            print("\nTop 5 Point Leaders: ( As of", now , ")")
            for count in range(userLoop):
                clickPoints = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Points']")))

                scroll_orgin = ScrollOrigin.from_element(clickPoints)
                ActionChains(driver)\
                    .scroll_to_element(clickPoints)\
                    .scroll_from_origin(scroll_orgin, 0, 200)\
                    .perform()
                time.sleep(0.5)

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
            print("\nError please try using a valid number.")

    userContinue = input("\nWant to continue: (y/n)\t").strip().lower()
    if(userContinue == 'n'):
        print("Closing...")
        driver.quit()
        break 
    elif(userContinue != 'y'):
        print("Invalid Input")
    
#if __name__ == '__main__':