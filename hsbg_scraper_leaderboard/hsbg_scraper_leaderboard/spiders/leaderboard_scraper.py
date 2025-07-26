import scrapy
import json


class LeaderboardApiSpider(scrapy.Spider):
    name = "leaderboard_api"
    allowed_domains = ["hearthstone.blizzard.com"]

    custom_settings = {
        "DOWNLOAD_DELAY": 0.1,  # ralentir un peu pour ne pas être trop agressif
        "CONCURRENT_REQUESTS": 8,
        "FEED_EXPORT_ENCODING": "utf-8",  # encodage clean pour CSV/JSON
    }

    def start_requests(self):
        total_pages = 50637
        base_url = "https://hearthstone.blizzard.com/en-us/api/community/leaderboardsData"
        for page in range(1, total_pages + 1):
            url = f"{base_url}?region=EU&leaderboardId=battlegrounds&seasonId=8&page={page}"
            yield scrapy.Request(url, callback=self.parse_page)

    def parse_page(self, response):
        try:
            data = json.loads(response.text)
            rows = data.get("leaderboard", {}).get("rows", [])
            for row in rows:
                yield {
                    "rank": row.get("rank"),
                    "accountid": row.get("accountid", ""),
                    "rating": row.get("rating"),
                }
        except Exception as e:
            self.logger.error(f"Erreur de parsing JSON: {e}")
