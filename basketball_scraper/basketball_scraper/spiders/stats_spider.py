import scrapy
import string

class StatsSpider(scrapy.Spider):
    name = "stats"
    rootUrl = "https://www.basketball-reference.com"

    start_urls = ["{}/players/{}/".format(rootUrl, l) for l in string.ascii_lowercase]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')