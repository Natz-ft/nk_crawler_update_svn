# -*- coding: utf-8 -*-
import re
from CrawlerModule import Crawler_URL
#from ContentAnalysis_multi_process import ContentAnalysis
from ContentAnalysis_multi_process_request import ContentAnalysis
#from ContentAnalysis_multi_process_refresh import ContentAnalysis
from test_config import parameter
import time
from collections import defaultdict
import copy
import utils
#from test_loop3 import isWaite_loop3
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Test:
    def __init__(self):
        self.result = defaultdict(list)
        
    def isRefresh(self,html_str):
        #hunanxiangzigongchengzixu_1_22_0
        #页面包含敏感关键字词 或者 域名没有备案号！
        #当前访问页面被阻断访问，请联系接入商！。。。。。123
        pass
    def getUrlList(self,model,parame,html_str,original_url,isloopBytime):
        if parame["number_xpath"] != "":
            next_type = parame["page_name"]["type"]  # 0:pageNo/page ;1:index_count.html ;2:post ;3:onclick;
            
            #获取一共的页数
            ori_number = model.number_page(parame["number_xpath"], html_str)
            if next_type != 2 and len(ori_number)==0:
                try:
                    model.driver.refresh()
                    WebDriverWait(model.driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, parame["number_xpath"])))
                    html_str = self.driver.page_source
                    ori_number = model.number_page(parame["number_xpath"], html_str)
                except:
                    print("getUrlList number_xpath is timeout ")                
            
            number = utils.retotalPage(ori_number)
            number = int(number)+1

            
            #控制页面
            print("total num is {}".format(number))
            for i in range(parame["page_name"]["startNum"], number):
                if parame["li"] != "":
                    #获取页面信息
                    bool = model.get_title_list(html_str, parame,isloopBytime=isloopBytime)
                else :
                    print("get_title_list is error")
                    return self.result
                #当页面发生错误时退出循环
                if bool == False :
                    break
                time.sleep(1)

                i = i+1
                if i==number:
                    continue
                tmp_parame = copy.deepcopy(parame["page_name"])
                if parame["page_name"] != "":
                    #将页数配置好
                    original_url = model.page_url(original_url, tmp_parame, i)
                else :
                    return self.result

                if next_type in [0,1]:
                    #获取页面信息
                    html_str = model.parse_url(original_url)                               
                else:
                    html_str = model.parse_url("",url_type=original_url,url_params=tmp_parame)
        else :
            isLoop = True
            next_type = parame["page_name"]["type"]
            i = parame["page_name"]["startNum"]
            while(isLoop):
                #if parame["li"] != "":
                #获取页面信息
                bool = model.get_title_list(html_str, parame,isloopBytime=isloopBytime)
                #else :
                    #return self.result
                #当页面发生错误时退出循环
                if bool == False :
                    isLoop = bool
                    break
                time.sleep(1)
                i = i+1

                tmp_parame = copy.deepcopy(parame["page_name"])
                if parame["page_name"] != "":
                    #将页数配置好
                    original_url = model.page_url(original_url, tmp_parame, i)
                else :
                    return self.result

                if next_type in [0,1]:
                    #获取页面信息
                    html_str = model.parse_url(original_url)                                       
                else:
                    html_str = model.parse_url("",url_type=original_url,url_params=tmp_parame)    

    def RunMain(self, url_info, key, html_name,vericode):
        #初始化
        model = Crawler_URL()
        parame = parameter[html_name]
        isloopBytime = True
        if "isloopBytime" in parame.keys():
            isloopBytime = parame["isloopBytime"]
        
        original_url = ""
        #get请求
        if isinstance(url_info,str):
            original_url = url_info        
        
            if parame["search"] != "" :
                original_url = model.Search(original_url, parame["search"])
            #获取页面信息
            html_str = model.parse_url(original_url)
            #print(html_str)
            self.getUrlList(model, parame, html_str, original_url,isloopBytime)
        elif isinstance(url_info,list):
            totalDimainUrl = []
            if isinstance(parame['domainName_url'],list):
                totalDimainUrl = copy.deepcopy(parame['domainName_url'])
            
            for i,url in enumerate(url_info):
                if isinstance(url,str):
                    original_url = url
                    if parame["search"] != "" :
                        original_url = model.Search(original_url, parame["search"])                    
                    html_str = model.parse_url(original_url)
                    if totalDimainUrl:
                        parame['domainName_url'] = totalDimainUrl[i]
                    self.getUrlList(model, parame, html_str, original_url,isloopBytime)
                else:
                    html_str = model.parse_url("",url_type=url_info["type"],url_params=url_info)
                    self.getUrlList(model, parame, html_str, original_url,isloopBytime)
        else:
            #获取页面信息
            html_str = model.parse_url("",url_type=url_info["type"],url_params=url_info)
            self.getUrlList(model, parame, html_str, original_url,isloopBytime)
        
        print("start ContentAnalysis")
        if ContentAnalysis(model,[]) :
        #if model.ContentAnalysis() :
            self.result = model.result()
        else:
            return self.result

        print(self.result)
        model.quit()
        return self.result



#if __name__ == "__main__":
    #test  = Test()
    #key = ["银行"]
    #test.RunMain("http://caigou.epicc.com.cn/epp-esp/notice/noticePageList?", key, "zhongguorenminbaoxian")