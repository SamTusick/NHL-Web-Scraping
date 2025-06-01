# NHL Scraper Functions

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time
import datetime

now = datetime.datetime.now().strftime("%B %d, %Y at %I:%M %p")

# Wait for Spinner to Close

def wait_for_spinner_to_disappear(wait):
    try:
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading-container")))
    except Exception as e:
        print("Spinner may not be present or already hidden:", e)

# Close Cookie Window

def close_cookie_window(driver, wait):
    try:
        # Checks to see if cookie banner is present
        cookieAccept = driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']")
        cookieAccept.click()
        print("\nCookie window close successfully!\n")

    except Exception as e:
        print("\nError finding or closing cookie banner: " , e, "\n") 

# Click Stat Tab

def click_stat_tab(driver, wait):

    wait_for_spinner_to_disappear(wait)
    statsElement = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Stats')]")))
    statsElement.click()

# Click Skater Section

def click_skater_section(driver, wait):

    wait_for_spinner_to_disappear(wait)
    skater_tab = wait.until(EC.element_to_be_clickable((By.ID, "skaters")))
    skater_tab.click()

# Goal Leaders Function

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

# Assist Leaders Function

def scrape_assist_leaders(driver, wait, count=5, is_first= True):
    print("Clicking Stat Tab...")
    click_stat_tab(driver, wait)

    print("Getting Skaters...")
    click_skater_section(driver, wait)

    print("Clicking Assists column...")

    click_goal = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Assists']")))
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
        click_goal = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Assists']")))
        click_goal.click()
    # Used for debugging
        print(f"Clicking Assists column... ({_+1}/{click_times})")
        time.sleep(0.5)

    # Grab the top N rows
    rows = driver.find_elements(By.XPATH, "//*[@id='season-tabpanel']//table/tbody/tr")

    
    leaders = []
    for i in range(min(count, len(rows))):
        name = rows[i].find_element(By.XPATH, "./td[2]/div/a").text
        assists = rows[i].find_element(By.XPATH, "./td[9]").text
        leaders.append({"name": name, "assists": assists})

    return {
        "title": f"Top {count} Assist Leaders (As of {now})",
        "leaders": leaders
    }

# Points Leaders Function

def scrape_points_leaders(driver, wait, count=5, is_first= True):
    print("Clicking Stat Tab...")
    click_stat_tab(driver, wait)

    print("Getting Skaters...")
    click_skater_section(driver, wait)

    print("Clicking Points column...")

    click_points = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Points']")))
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='season-tabpanel']//table")))

    scroll_origin = ScrollOrigin.from_element(click_points)
    ActionChains(driver)\
        .scroll_to_element(click_points)\
        .scroll_from_origin(scroll_origin, 0, 200)\
        .perform()
    time.sleep(0.5)

    click_times = 3 if is_first else 1
    for _ in range(click_times):
    # Re-select the element each time in case the DOM updates
        click_points = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Points']")))
        click_points.click()
    # Used for debugging
        print(f"Clicking Points column... ({_+1}/{click_times})")
        time.sleep(0.5)

    # Grab the top N rows
    rows = driver.find_elements(By.XPATH, "//*[@id='season-tabpanel']//table/tbody/tr")

    
    leaders = []
    for i in range(min(count, len(rows))):
        name = rows[i].find_element(By.XPATH, "./td[2]/div/a").text
        points = rows[i].find_element(By.XPATH, "./td[10]").text
        leaders.append({"name": name, "points": points})

    return {
        "title": f"Top {count} Points Leaders (As of {now})",
        "leaders": leaders
    }