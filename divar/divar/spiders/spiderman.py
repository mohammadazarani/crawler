import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader

from divar.items import DivarItem

class SpidermanSpider(CrawlSpider):
    name = 'spiderman'
    allowed_domains = ['divar']
    start_urls = ['https://divar.ir/v/%D8%B2%D9%85%DB%8C%D9%86-%D9%88%D8%A7%D9%85%D9%84%D8%A7%DA%A9_%D8%B2%D9%85%DB%8C%D9%86-%D9%88-%DA%A9%D9%84%D9%86%DA%AF%DB%8C_%DA%86%D8%A7%D8%A8%D9%87%D8%A7%D8%B1__%D8%AF%DB%8C%D9%88%D8%A7%D8%B1/wXIWH1Je']
    # start_urls = ['www.google.com']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # l.add_xpath('title', '//*[@itemprop="name"][1]/text()',
        #         MapCompose(unicode.strip, unicode.title))

        l = ItemLoader(item=DivarItem(), response=response)        

        #Done 
        l.add_xpath(advertismentTitle, '//h1[contains(@class, "page-title")][1]/text()', MapCompose(unicode.strip, unicode.title)) 
        print(advertismentTitle)
        #Done
        l.add_xpath(advertismentDescription, '//p[contains(@class, "post-description")][1]/text()') 

        # l.load_xpath(advertismentShortURL, '//h1[contains(@class, "page-title")][1]/text()]', MapCompose(unicode.strip, unicode.title)) 

        # l.load_xpath(houseArea, '//h1[contains(@class, "kt-unexpandable-row__value")][1]/text()', MapCompose(unicode.strip, unicode.title)) 


        # l.load_xpath(houseConstructionDate, '//h1[contains(@class, "page-title")][1]/text()]', MapCompose(unicode.strip, unicode.title)) 


        # l.load_xpath(houseCost, '//h1[contains(@class, "kt-unexpandable-row__value")][1]/text()]', MapCompose(unicode.strip, unicode.title)) 


        # l.load_xpath(houseLocation, '//h1[contains(@class, "page-title")][1]/text()]', MapCompose(unicode.strip, unicode.title)) 


        # l.load_xpath(houseRoomNumber, '//h1[contains(@class, "page-title")][1]/text()]', MapCompose(unicode.strip, unicode.title)) 


        # l.load_xpath(advertiser, '//h1[contains(@class, "page-title")][1]/text()]', MapCompose(unicode.strip, unicode.title)) 
        return l.load_item()     
