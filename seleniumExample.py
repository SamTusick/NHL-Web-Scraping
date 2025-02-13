from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

service = Service(PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")


print(driver.title)  # will print website title

search = driver.find_element(By.ID, "searchInput" ) # finds searchInput and saves it as search
search.send_keys("Pittsburgh Penguins") # types Pittsburgh Penguins into search 
search.send_keys(Keys.RETURN)   # presses enter

hof = driver.find_element(By.ID, "Hockey_Hall_of_Fame")
wait = WebDriverWait(driver, timeout=2)
wait.until(lambda _ : hof.is_displayed())

print(hof.text)

#time.sleep(5)   # keeps it open for 5 seconds



#driver.close()  # will close tab
driver.quit()   # will close whole website
