from scraper.spiders.jobs import BaseSpider


class PythonSpider(BaseSpider):
    name = "python"
    allowed_domains = ["nofluffjobs.com"]
    start_urls = ["https://nofluffjobs.com/"]

    def __init__(self, **kwargs):
        super().__init__("Python", **kwargs)
