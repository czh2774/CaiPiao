import scrapy,time,json
from ..items import fenxiItem

class fenxiSpider(scrapy.Spider):
    name="fenxi"
    url = 'http://i.sporttery.cn/wap/fb_match_info/get_result_his?mid='+'117174'+'&f_callback=getResultHistoryInfo&_=' + str(int(time.time() * 1000))
    start_urls=[url]

    def parse(self,response):
#        print(response)
        fx=fenxiItem()
        response=response.text
        respones = response[21:-2]
        respones = json.loads(respones)
        matchlist={}
        matchlist=respones['result']['data']
        match={}
        for match in matchlist:
            fx={}
            fx['come_from'] = 'fx'
            fx['match_id']=int(match['sporttery_matchid'])
            fx['date_cn'] = match['date_cn']
            fx['l_cn_abbr'] = match['l_cn_abbr']
            fx['h_cn_abbr'] = match['h_cn_abbr']
            fx['a_cn_abbr'] = match['a_cn_abbr']
            fx['final'] = match['final']
            fx['is_home'] = match['is_home']
            fx['mac_data'] = match['mac_data']



            yield fx
