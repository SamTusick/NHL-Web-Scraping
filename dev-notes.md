# 🏒 NHL Web Scraper — Developer Notes

## 🧪 To Run

1. Make sure ChromeDriver is installed and matches your Chrome version.
2. Open terminal and run:

```bash
python nhlScraper.py
```

---

## 📁 Project Structure

- `userMenu.py`
  Handles user input from the terminal. Displays a numbered menu of stat categories and returns the user's selection.

- `nhlScraper.py`
  Core scraping logic using Selenium. Launches browser, navigates NHL.com, scrapes the selected stats, and displays the top 5 players for goals, assists, or points.

---

## 🧠 Current Functionality

- Prompts user to choose a stat category (Goals, Assists, Points).
- Launches Chrome browser via Selenium WebDriver.
- Navigates to NHL stats page and selects "Skaters" tab.
- Closes the cookie pop-up (if it appears).
- Clicks the correct column to sort data based on the user selection.
- Scrapes top 5 players for the selected stat.
- Asks if the user wants to continue or quit.

---

## ⚙️ Requirements

- Python 3.x
- `selenium` library
- ChromeDriver installed and path correctly set in `PATH` variable:

## ✍️ Author

Samuel Tusick
Software Engineering Student @ Florida Gulf Coast University
Focus: Backend & AI
