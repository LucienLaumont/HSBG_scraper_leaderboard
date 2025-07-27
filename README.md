# 🎮 Hearthstone Battlegrounds – Leaderboard Analysis

> 📊 Dive into the Hearthstone Battlegrounds leaderboard data and uncover player performance insights!

---

## 🚀 Overview

With this repository, you can effortlessly retrieve and analyze leaderboard data from Blizzard’s official site:  
🔗 https://hearthstone.blizzard.com/fr-fr/community/leaderboards/?region=EU&leaderboardId=battlegrounds

- The leaderboard shows top players by **season** and **region** (EU, NA, ASIA).  
- **Currently**, only **Season 3 – EU** data has been collected (see `data/s3/eu/battlegrounds.csv`).  
- Feel free to gather other seasons or regions, but **please do not re-run** the scraper on already-extracted data to avoid overloading Blizzard’s public API.  

---

## 🛠️ Technologies

- **🐍 Python**  
- **🕸️ Scrapy**  
- **🐼 pandas**  
- **📈 matplotlib**

---

## 📥 Data Structure

```

data/
└── s3/
└── eu/
└── battlegrounds.csv   # Season 3 – EU leaderboard export

````

---

## ▶️ Running the Scraper

1. Navigate to the scraper directory:  
   ```bash
   cd hsbg_scraper_leaderboard
    ```

2. Activate your virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Launch the Scrapy spider:

   ```bash
   scrapy crawl leaderboard -o data/s3/eu/battlegrounds.csv
   ```