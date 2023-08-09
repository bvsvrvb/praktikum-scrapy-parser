import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import SPIDER_NAME, ALLOWED_DOMAINS, START_URLS


class PepSpider(scrapy.Spider):
    name = SPIDER_NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        rows = response.css('section#numerical-index tbody tr')
        for row in rows:
            pep_link = row.css('a::attr(href)').get()
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.css('h1.page-title::text').get().split(' – ')
        data = {
            'number': int(number.replace('PEP ', '')),
            'name': name,
            'status': response.css('dd abbr::text').get()
        }
        yield PepParseItem(data)
