# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SteamcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    steam_appid = scrapy.Field()
    price_overview = scrapy.Field()
    genres = scrapy.Field()
    release_date = scrapy.Field()
    crawl_date = scrapy.Field()
    