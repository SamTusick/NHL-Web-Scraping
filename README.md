# 🏒 NHL Web Scraper

A Python + React tool that scrapes real-time NHL data by category using Selenium. Built for quick access to different player stat leaders.

## 🎥 Demo

A demo video can be found here: [coming soon]

## 🧪 Usage

Once both servers are running, you can interact with the app via the frontend. It makes API calls to the Flask backend to fetch NHL stats. Progress checkpoints and scraping updates will appear in the backend terminal.

## 🛠 Prerequisites

- [Node.js](https://nodejs.org/) installed
- [Python 3.9+](https://www.python.org/) installed
- `pip` and `venv` available

## 🚀 Getting Started

You will need **two separate terminals** to run this program.

### 1. Clone the Repository

```bash
git clone https://github.com/SamTusick/NHL-Web-Scraping.git
cd NHL-Web-Scraping
```
### 2. Set Up the Frontend (Terminal 1)

```bash
cd frontend/nhl-stat-frontend
npm install
npm run dev
```

### 3. Set Up the Backend (Terminal 2)

```bash
cd NHL-Web-Scraping
python -m venv .venv
source .venv/Scripts/activate   # On Windows
# or
source .venv/bin/activate       # On macOS/Linux

pip install -r requirements.txt
python app.py
```
