# Flask API

# app.py
from flask import Flask, jsonify, request
from scraper.driver import get_driver
from scraper.scraper_functions import scrape_goal_leaders  
from scraper.scraper_functions import close_cookie_window  

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the NHL Stats API!"})

@app.route("/stats/goals", methods=["GET"])
def get_goal_stats():
    count = request.args.get("count", default=5, type=int)

    count = 6

    driver, wait = get_driver()
    driver.get("https://www.nhl.com")
    driver.maximize_window()

    try:
        close_cookie_window(driver, wait)
        data = scrape_goal_leaders(driver, wait, count, is_first=True) 
        return jsonify(data)
    finally:
        driver.quit()

if __name__ == "__main__":
    app.run(debug=True)
