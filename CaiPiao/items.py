# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class bifenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    match_zhu = scrapy.Field()
    match_ke = scrapy.Field()
    match_id = scrapy.Field()
    match_time = scrapy.Field()
    match_name = scrapy.Field()
    match_begin = scrapy.Field()
    match_zhu_id = scrapy.Field()
    match_ke_id = scrapy.Field()
    match_week = scrapy.Field()
    match_minute = scrapy.Field()
    match_quan_zhu = scrapy.Field()
    match_quan_ke = scrapy.Field()
    match_ban_zhu = scrapy.Field()
    match_ban_ke = scrapy.Field()
    match_status = scrapy.Field()
    #pass

class fenxiItem(scrapy.Item):
    match_id = scrapy.Field()
    date_cn = scrapy.Field()
    l_cn_abbr = scrapy.Field()
    h_cn_abbr = scrapy.Field()
    a_cn_abbr = scrapy.Field()
    final = scrapy.Field()
    is_home = scrapy.Field()
    mac_data = scrapy.Field()

