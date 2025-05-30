# Dev Notes — NHL Web Scraper

## Weekend Plan (June 1–2)

- [x] Review existing `userMenu.py` and `nhlScraper.py`
- [x] Add `headless` mode to Selenium
- [ ] Clean up XPath selectors for stability
- [x] Create initial README.md with overview and instructions

---

## Weekly Plan (June 3–9)

### 🧱 Backend Prep

- [ ] Refactor scraper into functions (goals, assists, points)
- [ ] Set up Python virtual environment
- [ ] Install and configure Flask
- [ ] Create base Flask route to test connection
- [ ] Build first API route: `/stats/goals`

---

### ⚛️ Frontend (Coming Soon)

- [ ] Scaffold new React app
- [ ] Create simple homepage with stat selection
- [ ] Connect to Flask backend via fetch
- [ ] Display JSON results in a table

---

## 📝 Notes to Self

- Keep frontend and backend loosely coupled
- Selenium can be slow — consider caching results later
- Use `print()` or logging to test API endpoints before integrating with React
- Keep `PATH` to ChromeDriver portable for easier deployment

---

## 🐛 Issues to Watch

- NHL site layout may change and break XPath
- Long scraping time could cause API timeout
- Clicking elements may fail if not visible — use `WebDriverWait`

---

## 💡 Ideas for Later

- Add dropdown for selecting team or player stats
- Allow user to export results to `.csv`
- Add authentication layer for protected routes
- Schedule scraper to run periodically and store results (cron job or background task)

---

## ⚙️ Tech Stack Plan

| Layer    | Tech                      | Purpose                |
| -------- | ------------------------- | ---------------------- |
| Frontend | React                     | User interface         |
| Backend  | Flask (Python)            | API to trigger scraper |
| Scraper  | Selenium                  | Scraping NHL.com stats |
| Storage  | (Optional) SQLite or JSON | Cache results          |

---

## 🔗 Reference Links

- [NHL Stats Page](https://www.nhl.com/stats/)
- [Selenium Docs](https://www.selenium.dev/documentation/)
- [Flask Docs](https://flask.palletsprojects.com/)

---

## Where to Continue

- Set up Flask with one working `/stats` route
- Test returning hardcoded JSON before scraping
- Then plug in scraper logic and return real-time data
