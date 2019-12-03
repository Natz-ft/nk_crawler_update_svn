# -*- coding: utf-8 -*-
import re
from CrawlerModule import Crawler_URL
#from ContentAnalysis_multi_process import ContentAnalysis
#from ContentAnalysis_multi_process_request import ContentAnalysis
from ContentAnalysis_multi_process_refresh import ContentAnalysis
from importlib import reload
import test_config
import time
from collections import defaultdict
import copy
import utils
#from test_loop3 import isWaite_loop3

# post 请求 json
class TestJson:
    def __init__(self):
        self.result = defaultdict(list)
        

      

    def RunMain(self, url_info, key, html_name,vericode):
        reload(test_config)
        #初始化
        model = Crawler_URL()
        parame = test_config.parameter[html_name]
        isloopBytime = True
        if "isloopBytime" in parame.keys():
            isloopBytime = parame["isloopBytime"]
        
        original_url = ""
        url_type = ''
        if isinstance(url_info,str):
            original_url = url_info
            html_str = model.parse_url_2(original_url)
            url_type = 'get'
        else:
            html_str = model.parse_url_2('',url_type="post",url_params=url_info)
            url_type = 'post'
        
        if parame["number_xpath"]=="":
            isloop=True
            i = parame["page_name"]["startNum"]
            tmp_parame = copy.deepcopy(parame["page_name"])
            while(isloop):
               
                #获取页面信息
                bool = model.get_title_list_2(html_str, parame)
                #当页面发生错误时退出循环
                if bool == False :
                    isloop = False
                    break
                time.sleep(1)
                i = i+1
                #获取下一页
                if url_type == 'post':
                    replaceKey = parame["page_name"]["replace"]
                    url_info['data'][replaceKey] = i
                    url_info['data']['begin'] = i*10
                    html_str = model.parse_url_2('',url_type="post",url_params=url_info)
                else:
                    original_url = model.page_url(original_url, tmp_parame, i) 
                    html_str = model.parse_url_2(original_url)
                
                
        if ContentAnalysis(model,[]) :
        #if model.ContentAnalysis() :
            self.result = model.result()
            
        if len(self.result)==0 and len(model.content_item['网址']) >0:
            model.content_item['时间信息'] = [[]] * len(model.content_item['网址'])
            self.result = model.result()

        print(self.result)
        model.quit()
        return self.result



#if __name__ == "__main__":
    #test  = Test()
    #key = ["银行"]
    #test.RunMain("http://caigou.epicc.com.cn/epp-esp/notice/noticePageList?", key, "zhongguorenminbaoxian")