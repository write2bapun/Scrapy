from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem

class MySpider(BaseSpider):
    name = "craig"
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://chicago.craigslist.org/search/cta"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//span[@class='txt']")
        #titles = hxs.select("//span[@class='pl']")
        for titles in titles:
            #title = titles.select("a/text()").extract()
            #link = titles.select("a/@href").extract()
            #time = titles.select(".//span[@class='pl']/time[@datetime]/text()").extract()
            time = titles.select(".//time/@datetime").extract() 
            title = titles.select(".//span[@class='pl']/a/text()").extract()
            link = titles.select(".//span[@class='pl']/a/@href").extract()
            price = titles.select(".//span[@class='price']/text()").extract()
            print time, title, link, price