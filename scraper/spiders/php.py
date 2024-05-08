from scraper.spiders.base_spider import BaseSpider


class PHPSpider(BaseSpider):
    name = "php"
    allowed_domains = ["nofluffjobs.com"]
    start_urls = ["https://nofluffjobs.com/"]

    def __init__(self, **kwargs):
        super().__init__("PHP", **kwargs)
