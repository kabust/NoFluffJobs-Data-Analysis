import time

import scrapy
from scrapy.http import Response

from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By

from .job_parser import JobParser


class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["nofluffjobs.com"]
    start_urls = ["https://nofluffjobs.com/Python"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_url = "https://nofluffjobs.com/Python"

    def parse(self, response: Response, **kwargs):
        urls = self._get_urls()

        for url in urls:
            yield scrapy.Request(url, callback=self._scrape_single_job)

    def _scrape_single_job(self, response: Response) -> dict:
        job_parser = JobParser(response)

        yield job_parser.get_job_dictionary()

    def _get_urls(self):
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)

        driver.get(self.main_url)
        time.sleep(1)

        try:
            if accept := driver.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler"):
                accept.click()
        except NoSuchElementException:
            pass

        while True:
            try:
                button = driver.find_element(
                    By.CSS_SELECTOR,
                    "div.tw-flex.tw-flex-wrap.tw-justify-center.tw-my-8.tw-gap-4.ng-star-inserted > button"
                )
                button.click()
            except (NoSuchElementException, StaleElementReferenceException):
                break

        urls = [
            url.get_attribute("href")
            for url in driver.find_elements(By.CSS_SELECTOR, ".list-container.ng-star-inserted > a")
        ]

        driver.quit()

        return urls
