# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class bifenPipeline(object):
    def open_spider(self,spider):
        self.con=sqlite3.connect("caipiao.db")
        self.cu=self.con.cursor()
    def process_item(self, item, spider):
        print(item['come_from'])
        if item['come_from']=='bf':
            insert_sql="insert into bifen(match_id,match_name,match_begin,match_time,match_week,match_zhu,match_zhu_id,match_ke,match_ke_id,match_minute,match_quan_zhu,match_quan_ke,match_ban_zhu,match_ban_ke,match_status) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(item['match_id'],item['match_name'],item['match_begin'],item['match_time'],item['match_week'],item['match_zhu'],item['match_zhu_id'],item['match_ke'],item['match_ke_id'],item['match_minute'],item['match_quan_zhu'],item['match_quan_ke'],item['match_ban_zhu'],item['match_ban_ke'],item['match_status'])
        else:
            insert_sql = "insert into fenxiguanxi(match_id,date_cn,l_cn_abbr,h_cn_abbr,a_cn_abbr,final,is_home,mac_data) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(item['match_id'], item['date_cn'], item['l_cn_abbr'], item['h_cn_abbr'], item['a_cn_abbr'], item['final'],item['is_home'], item['mac_data'])

        self.cu.execute(insert_sql)

        self.con.commit()
        return item
    def spider_close(self,spider):
        self.con.close()

