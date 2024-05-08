from scraper.spiders.base_spider import BaseSpider


class JavaSpider(BaseSpider):
    name = "java"
    allowed_domains = ["nofluffjobs.com"]
    start_urls = ["https://nofluffjobs.com/"]

    def __init__(self, **kwargs):
        super().__init__("Java", **kwargs)
