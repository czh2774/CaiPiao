import scrapy,time,json
from ..items import bifenItem

class bifenSpider(scrapy.Spider):
    name="bifen"
    url = 'http://i.sporttery.cn/api/match_live_2/get_match_list?callback=?&_=' + str(int(time.time() * 1000))
    start_urls=[url]

    def parse(self,response):
#        print(response)
        jcw=bifenItem()
        response=response.text
        response=response[17:-1]
        response=json.loads(response)
        match_id_list=list(response)
        for match_id in match_id_list:
            result=response[match_id]
            jcw={}
            jcw['come_from']='bf'
            jcw['match_id']=int(match_id[1:])
            jcw['match_name'] = result['l_cn']
            jcw['match_begin'] = result['time_cn']
            jcw['match_time'] = result['date_cn']
            jcw['match_week'] = result['match_num'][:2]
            jcw['match_zhu'] = result['h_cn']
            jcw['match_zhu_id'] = result['l_id']
            jcw['match_ke'] = result['a_cn']
            jcw['match_ke_id'] = result['h_id']
            jcw['match_minute']=result['minute']
            jcw['match_quan_zhu']=result['fs_h']
            jcw['match_quan_ke']=result['fs_a']
            jcw['match_ban_zhu']=result['hts_h']
            jcw['match_ban_ke']=result['hts_a']
            jcw['match_status']=result['status']


            yield jcw
