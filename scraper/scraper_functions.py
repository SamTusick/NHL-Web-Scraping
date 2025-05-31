# NHL Scraper Functions

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time
import datetime

now = datetime.datetime.now().strftime("%B %d, %Y at %I:%M %p")

def close_cookie_window(driver, wait):
    try:
        #checks to see if cookie banner is present
        cookieAccept = driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']")
        cookieAccept.click()
        print("\nCookie window close successfully!\n")

    except Exception as e:
        print("\nError finding or closing cookie banner: " , e, "\n") 

def click_stat_tab(driver, wait):
    statsElement = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Stats')]")))
    statsElement.click()

def click_skater_section(driver, wait):
    skater_tab = wait.until(EC.element_to_be_clickable((By.ID, "skaters")))
    skater_tab.click()

def scrape_goal_leaders(driver, wait, count=5, is_first=True):
    print("Clicking Stat Tab...")
    click_stat_tab(driver, wait)

    print("Getting Skaters...")
    click_skater_section(driver, wait)

    print("Clicking Goals column...")

    click_goal = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Goals']")))
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='season-tabpanel']//table")))

    scroll_origin = ScrollOrigin.from_element(click_goal)
    ActionChains(driver)\
        .scroll_to_element(click_goal)\
        .scroll_from_origin(scroll_origin, 0, 200)\
        .perform()
    time.sleep(0.5)

    click_times = 3 if is_first else 1
    for _ in range(click_times):
    # Re-select the element each time in case the DOM updates
        click_goal = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Goals']")))
        click_goal.click()
    # Used for debugging
        print(f"Clicking goals column... ({_+1}/{click_times})")
        time.sleep(0.5)

    # Grab the top N rows
    rows = driver.find_elements(By.XPATH, "//*[@id='season-tabpanel']//table/tbody/tr")

    
    leaders = []
    for i in range(min(count, len(rows))):
        name = rows[i].find_element(By.XPATH, "./td[2]/div/a").text
        goals = rows[i].find_element(By.XPATH, "./td[8]").text
        leaders.append({"name": name, "goals": goals})

    return {
        "title": f"Top {count} Goal Leaders (As of {now})",
        "leaders": leaders
    }

def scrape_assist_leaders(driver, wait, count=5, is_First= True):
    print("Clicking Stat Tab...")
    click_stat_tab(driver, wait)

    print("Getting Skaters...")
    click_skater_section(driver, wait)

    print("Clicking Goals column...")

    click_goal = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Goals']")))
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='season-tabpanel']//table")))

    scroll_origin = ScrollOrigin.from_element(click_goal)
    ActionChains(driver)\
        .scroll_to_element(click_goal)\
        .scroll_from_origin(scroll_origin, 0, 200)\
        .perform()
    time.sleep(0.5)

    click_times = 3 if is_first else 1
    for _ in range(click_times):
    # Re-select the element each time in case the DOM updates
        click_goal = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Goals']")))
        click_goal.click()
    # Used for debugging
        print(f"Clicking goals column... ({_+1}/{click_times})")
        time.sleep(0.5)

    # Grab the top N rows
    rows = driver.find_elements(By.XPATH, "//*[@id='season-tabpanel']//table/tbody/tr")

    
    leaders = []
    for i in range(min(count, len(rows))):
        name = rows[i].find_element(By.XPATH, "./td[2]/div/a").text
        goals = rows[i].find_element(By.XPATH, "./td[8]").text
        leaders.append({"name": name, "goals": goals})

    return {
        "title": f"Top {count} Assist Leaders (As of {now})",
        "leaders": leaders
    }