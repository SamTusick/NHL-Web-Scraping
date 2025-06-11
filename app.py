# Flask API

# app.py
from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from scraper.scraper_functions import (
     scrape_stat_leaders,
     close_cookie_window  
)

app = Flask(__name__)

# Driver SetUp Function

def setup_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 15)

    return driver, wait

# Main Page

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the NHL Stats API!"})

# Skater Goal Leaders

@app.route("/stats/skater/goals", methods=["GET"])
def get_goal_stats():
    
    print("Setting Up Driver...")
    driver, wait = setup_driver()

    count = request.args.get("count", default=5, type=int)

    count = 6

    driver.get("https://www.nhl.com")

    try:
        close_cookie_window(driver, wait)
        data = scrape_stat_leaders(driver, wait, stat_title = "Goals", column_index = 8, label = "goals", count=count, is_first=True)

        return jsonify(data)
    finally:
        driver.quit()

# Skater Assists Leaders

@app.route("/stats/skater/assists", methods=["GET"])
def get_assists_stats():

    print("Setting Up Driver...")
    driver, wait = setup_driver()

    count = request.args.get("count", default=5, type=int)

    count = 6

    driver.get("https://www.nhl.com")

    try:
        close_cookie_window(driver, wait)
        data = scrape_stat_leaders(driver, wait, stat_title = "Assists", column_index = 9, label = "assists", count=count, is_first=True)

        return jsonify(data)
    finally:
        driver.quit()

# Skater Point Leaders

@app.route("/stats/skater/points", methods=["GET"])
def get_points_stats():

    print("Setting Up Driver..")
    driver, wait = setup_driver()

    count = request.args.get("count", default=5, type=int)

    count = 6

    driver.get("https://www.nhl.com")

    try:
        close_cookie_window(driver, wait)
        data = scrape_stat_leaders(driver, wait, stat_title = "Points", column_index = 10, label = "points", count=count, is_first=True)

        return jsonify(data)
    finally:
        driver.quit()

if __name__ == "__main__":
    app.run(debug=True)
