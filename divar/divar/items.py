# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html




import scrapy


class DivarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    advertismentTitle = scrapy.Field()
    advertismentDescription = scrapy.Field()
    # advertismentShortURL = scrapy.Field()

    # houseArea = scrapy.Field()
    # houseConstructionDate = scrapy.Field()
    # houseCost = scrapy.Field()
    # houseLocation = scrapy.Field()
    # houseRoomNumber = scrapy.Field()
    
    # advertiser = scrapy.Field(//h1[contains(@class, 'page-title')])+
