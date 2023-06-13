import scrapy


class HotspotsSpider(scrapy.Spider):
    name = "hotspots"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        hotspots = response.css('span.title-content-title::text').getall()
        for hotspot in hotspots:
            yield {
                'title': hotspot
            }
