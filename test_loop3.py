# -*- coding: utf-8 -*-
import re
from CrawlerModule import Crawler_URL
#from ContentAnalysis_multi_process import ContentAnalysis
from ContentAnalysis_multi_process_request import ContentAnalysis
from test_config import parameter
import time
from collections import defaultdict
import copy
import time
from utils import isLogin_byXpath,retotalPage

class Test_loop3:
    def __init__(self):
        self.result = defaultdict(list)

    def RunMain(self, url_info, key, html_name):
        #初始化
        model = Crawler_URL()
        parame = parameter[html_name]
        isloopBytime = True
        if "isloopBytime" in parame.keys():
            isloopBytime = parame["isloopBytime"]
        
        #登陆
        login_infos = [url_info["url"], parame["login"]]
        driver = model.log_in_web(*login_infos)
        
        #生成需要  获取的查询列表
        #h_lx
        #0：全部 1：招标信息 2：采购信息 3：项目信息
        urlList = [url_info["formatUrl"].format(j, i) for i in range(1, 3) for j in url_info["include_keys"]]
        
        for original_url in urlList:
            
            #获取页面信息
            html_str = model.parse_url(original_url)
            if parame["number_xpath"] != "":
                #获取一共的页数
                num_str = model.number_page(parame["number_xpath"], html_str)
                
                num_str = ''.join(re.findall(r'\d+', "".join(num_str)))
                num_page = int(int(num_str) / 20) + 1                
                for i in range(parame["page_name"]["startNum"], num_page):
                    if parame["li"] != "":
                        #获取页面信息
                        bool = model.get_title_list(html_str, parame["li"],parame["li_time"], parame["title"], parame["href"], parame["domainName_url"], parame["li_area"],isloopBytime=isloopBytime)
                    else :
                        return self.result
                    #当页面发生错误时退出循环
                    if bool == False :
                        break
                    
                    time.sleep(1)
                                        
                    i = i+1
                    if i==num_page:
                        continue
                    tmp_parame = copy.deepcopy(parame["page_name"])
                    if parame["page_name"] != "":
                        #将页数配置好
                        original_url = model.page_url(original_url, tmp_parame, i)
                    else :
                        return self.result
                    #获取页面信息
                    html_str = model.parse_url(original_url)
                    
                   
        #if ContentAnalysis(model,login_infos) :
        if model.ContentAnalysis() :
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