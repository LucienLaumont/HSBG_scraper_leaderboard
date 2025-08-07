import scrapy
import json

SEASON = 15
REGION = "EU"


class LeaderboardApiSpider(scrapy.Spider):
    name = "leaderboard_api"
    allowed_domains = ["hearthstone.blizzard.com"]
    base_url = "https://hearthstone.blizzard.com/en-us/api/community/leaderboardsData"

    custom_settings = {
        "DOWNLOAD_DELAY": 0.1,
        "CONCURRENT_REQUESTS": 8,
        "FEED_EXPORT_ENCODING": "utf-8",
    }

    def start_requests(self):
        # On ne démarre que sur la page 1
        url = (
            f"{self.base_url}"
            f"?region={REGION}"
            f"&leaderboardId=battlegrounds"
            f"&seasonId={SEASON}"
            f"&page=1"
        )
        yield scrapy.Request(url, callback=self.parse_page, meta={"page": 1})

    def parse_page(self, response):
        page = response.meta["page"]
        try:
            data = json.loads(response.text)
            rows = data.get("leaderboard", {}).get("rows", [])
        except Exception as e:
            self.logger.error(f"Erreur de parsing JSON à la page {page}: {e}")
            return

        if not rows:
            self.logger.info(f"Aucune donnée à la page {page}, fin de la pagination.")
            return

        # On émet les items
        for row in rows:
            yield {
                "rank": row.get("rank"),
                "accountid": row.get("accountid", ""),
                "rating": row.get("rating"),
            }

        # Si on a des données, on demande la page suivante
        next_page = page + 1
        next_url = (
            f"{self.base_url}"
            f"?region={REGION}"
            f"&leaderboardId=battlegrounds"
            f"&seasonId={SEASON}"
            f"&page={next_page}"
        )
        yield scrapy.Request(
            next_url,
            callback=self.parse_page,
            meta={"page": next_page},
        )
