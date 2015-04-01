#This script is to use Xpath. To run it use --> scrapy crawl craig_obj_xpath -o Craig_Out.csv
#Author: Sam
from scrapy.spider import BaseSpider #Base Spider has basic functionality
from scrapy.selector import Selector #Selector to use Xpath. Another type of parser
#from scrapy.selector import HtmlXPathSelector # One type of parser to parse HTML
from craigslist_sample_obj.items import CraigslistSampleObjItem


class MySpider(BaseSpider):
    name = "craig_obj_xpath"
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://chicago.craigslist.org/search/cta"]

    def parse(self, response):
        #hxs = HtmlXPathSelector(response) #HtmlXPathSelector
        #titles = hxs.xpath("//span[@class='txt']") #HtmlXPathSelector
        titles = response.selector.xpath("//span[@class='txt']") #Selector
        items = []
        for titles in titles:
            item = CraigslistSampleObjItem()
            item["time"] = titles.xpath(".//time/@datetime").extract() #Selector
            item["title"] = titles.xpath(".//span[@class='pl']/a/text()").extract() #Selector #Selector
            item["link"] = titles.xpath(".//span[@class='pl']/a/@href").extract() #Selector
            item["price"] = titles.xpath(".//span[@class='price']/text()").extract() #Selector
            
            #item["time"] = titles.select(".//time/@datetime").extract() 
            #item["title"] = titles.select(".//span[@class='pl']/a/text()").extract()
            #item["link"] = titles.select(".//span[@class='pl']/a/@href").extract()
            #item["price"] = titles.select(".//span[@class='price']/text()").extract()
            items.append(item)
            #print time, title, link, price
        return items