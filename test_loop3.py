# -*- coding: utf-8 -*-
import re
from CrawlerModule import Crawler_URL
#from ContentAnalysis_multi_process import ContentAnalysis
#from ContentAnalysis_multi_process_request import ContentAnalysis
from ContentAnalysis_multi_process_refresh import ContentAnalysis
from test_config import parameter
import time
from collections import defaultdict
import copy
import time
from utils import isLogin_byXpath,retotalPage
#from test_config import content_wait_func_dic
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait(driver):
    return not ('您访问频率太高' in driver.page_source)
def isWaite_loop3(driver):

    try:
        WebDriverWait(driver, 10).until(wait, 'decode_captcha fail to find yzm')
    except:
        # 如果不显示正常页面，刷新页面
        while not wait:
            print('您访问频率太高：refresh page...')
            driver.refresh()
            time.sleep(5)

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
            if html_str == "":
                print("{} parse_url is empty ".format(original_url))
                continue
            if parame["number_xpath"] != "":
                #获取一共的页数
                num_str = model.number_page(parame["number_xpath"], html_str)
                
                num_str = ''.join(re.findall(r'\d+', "".join(num_str)))
                if num_str =='':
                    continue
                num_page = int(int(num_str) / 20) + 1                
                for i in range(parame["page_name"]["startNum"], num_page):
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
                    if '您访问频率太高' in html_str:
                        model.driver.refresh()
                        time.sleep(5)
                        html_str = model.parse_url(original_url)
                        for loop_i in range(3):
                            if '您访问频率太高' in html_str:
                                model.driver.refresh()
                                time.sleep(5)
                                html_str = model.parse_url(original_url)
                            else:
                                break
        
        wait_fuc_name = ''  
        
        #if "content_wait_class" in parame.keys():
            #wait_fuc_name = parame["content_wait_class"] #return 'isWaite_loop3'

        if ContentAnalysis(model,login_infos,wait_foc_func=isWaite_loop3) :
        #if model.ContentAnalysis(content_wait_func_dic[wait_fuc_name]) :
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