# -*- coding: utf-8 -*-
import re
from CrawlerModule import Crawler_URL
from ContentAnalysis_multi_process_refresh import ContentAnalysis
#from ContentAnalysis_multi_process import ContentAnalysis
#from ContentAnalysis_multi_process_request import ContentAnalysis
from test_config import parameter
import time
from collections import defaultdict
import copy
import time
from utils import isLogin_byXpath,retotalPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Test_login:
    def __init__(self):
        self.result = defaultdict(list)
        
        
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
                    
            number = retotalPage(ori_number)
            number = int(number)+1
            
            next_type = parame["page_name"]["type"]  # 0:pageNo/page ;1:index_count.html ;2:post ;3:onclick;
            
            #number = 2
            #控制页面
            for i in range(parame["page_name"]["startNum"], number):
                if parame["li"] != "":
                    #获取页面信息
                    bool = model.get_title_list(html_str, parame,isloopBytime=isloopBytime)
                else :
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
        login_infos = [url_info, parame["login"],vericode]
        #登陆
        driver = model.log_in_web(*login_infos)
        
        isLogin = globals()[parame["login"]["login_status"]["class"]](driver,parame["login"]["login_status"]["params"])        
       
        
        #判断失败： 验证码错误 循环（maxnum =5)
        if not isLogin:
            count = 0
            for i in range(3):
                driver = model.log_in_web(*login_infos)
                isLogin = globals()[parame["login"]["login_status"]["class"]](driver,parame["login"]["login_status"]["params"]) 
                if isLogin:
                    break
                count = count+1
            if count == 2:
                print("{} is login error".format(html_name))
                #return self.result
    
        #判断成功
        #self.cookie_info = self.driver.get_cookies()                     # 列表中包含多个字典
        #self.cookie_dict = {i["name"]: i["value"] for i in self.cookie_info}  # 字典推导式
        #response = requests.get(href_title, headers=self.headers,cookies=self.cookie_dict)
        if "startPage_pre"  in  parame.keys():
            pageType = parame["startPage_pre"]["type"]
            if pageType=="get":
                html_str = model.parse_url(parame["startPage_pre"]["url"])
        if isinstance(parame["startPage"],list):
            for item in parame["startPage"]:
                if item["type"]=="get":
                    original_url = item["url"]
                    html_str = model.parse_url(original_url)
                    self.getUrlList(model, parame, html_str, original_url,isloopBytime)
                elif item["type"]=="onclick":
                    #获取页面信息
                    html_str = model.parse_url("",url_type=item["type"],url_params=item)
                    self.getUrlList(model, parame, html_str, original_url,isloopBytime)
        else:
            if parame["startPage"]["type"]=="get":
                original_url = parame["startPage"]["url"]
                #获取页面信息
                html_str = model.parse_url(original_url)
            else:    
                
                html_str = model.parse_url("",url_type=parame["startPage"]["type"],url_params=parame["startPage"])
            self.getUrlList(model, parame, html_str, original_url,isloopBytime) 
            
        print("start ContentAnalysis")   
        login_infos = [url_info, parame["login"],None]
        if ContentAnalysis(model,login_infos) :
        #if model.ContentAnalysis() :
            self.result = model.result()
        else:
            return self.result

        print(self.result)
        model.quit()
        return self.result



if __name__ == "__main__":
    test  = Test()
    key = ["银行"]
    test.RunMain("http://caigou.epicc.com.cn/epp-esp/notice/noticePageList?", key, "zhongguorenminbaoxian")