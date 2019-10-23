# -*- coding: utf-8 -*-
import re
from lxml import etree
from selenium import webdriver
import time
import datetime
from fake_useragent import UserAgent
from collections import defaultdict
import random
import platform
from config import config
from utils import filter_title, regex, rehref
import urllib.request
import urllib.parse
import requests

class Crawler_URL:
    def __init__(self):  # 初始化url_array;启动web_drive
        self.headers = {"User-Agent": UserAgent().chrome}
        # 创建存储信息的列表
        self.content_item = defaultdict(list)
        # 加载chromedriver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--allow-file-access-from-files")
        #chrome_options.add_argument('--headless')  #服务器上不注释
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--no-sandbox")
        platform_info = platform.platform()
        platform_info = ''.join(re.findall(r'Windows', platform_info))

        if platform_info == "Windows":
            self.driver = webdriver.Chrome(config.driver_windows, chrome_options=chrome_options)
        else:
            self.driver = webdriver.Chrome(config.driver_linux, chrome_options=chrome_options)
            


    # 登陆浏览器
    def log_in_web(self, userName, userpwd):
        self.driver.get()
        time.sleep(3)
        self.driver.find_element_by_id("username").send_keys(userName)
        self.driver.find_element_by_id("userpwd").send_keys(userpwd)
        self.driver.find_element_by_class_name("submit").click()
        time.sleep(1)
        
        
    # 得到html字符串
    def parse_url(self, href_title,url_type="get",url_params={}):
        if url_type=="get":
            # 发送selenium请求
            self.driver.get(href_title)
            html_str = self.driver.page_source
        elif url_type=="post":
            response = requests.post(url_params["post_url"], headers=url_params["headers"],  data=url_params["data"], verify=False)
            html_str = str(response.content, encoding="utf-8")
        elif url_type=="onclick":
            click_params = url_params["onclick"]
            for url_param in click_params:
                if "url" in url_param.keys():               
                    self.driver.get(url_param["url"])
                    time.sleep(3)
                params= url_param["params"]
                if len(params)==0:
                    self.driver.find_element_by_xpath(url_param["button"]).click()
                else:
                    for tmp_param in params:
                        if tmp_param["type"]=="id":
                            self.driver.find_element_by_id(tmp_param["name"]).send_keys(tmp_param["value"])
                        elif tmp_param["type"]=="class":
                            self.driver.find_element_by_class_name(tmp_param["name"]).send_keys(tmp_param["value"])
                        elif tmp_param["type"]=="xpath":
                            self.driver.find_elements_by_xpath(tmp_param["name"]).send_keys(tmp_param["value"])
                        time.sleep(1)
                    self.driver.find_element_by_xpath(url_param["button"]).click()
                time.sleep(2)
            html_str = self.driver.page_source
            #html_str = str(content, encoding="utf-8")
        return html_str
    

    # 4.提取标题（将需要的标题先保存下来）
    def get_title_list(self, page_html_str, li, li_time, title, href, domainName_url = None, li_area = None,isloopBytime=True):
        try:
            # 把html字符串转换成element对象
            html_element = etree.HTML(page_html_str)
            
            #行信息
            li_list = html_element.xpath(li)

            #当页面信息为0的时候，结束爬虫
            if len(li_list) == 0:
                print("li_list:", len(li_list))
                return False

            # 遍历所有li元素
            for li in li_list[0:]:
                # 获取项目发布日期
                stime = "".join(li.xpath(li_time))

                if stime == "":
                    continue

                #时间处理
                p = re.compile('(\d{4}[年，-]\d{1,2}[月,-]\d{1,2})')
                submit_time = p.findall(stime)[0]
                
                if isloopBytime:
                    # 昨天日期
                    today = datetime.date.today()
                    yesterday = str(today - datetime.timedelta(days=1))
                    #yesterday = str(today)
                    #发布的时间不是昨天的时间，就结束本次循环
                    
                    if submit_time > yesterday:
                        continue
                    elif submit_time < yesterday:
                        return False

                # 获取项目标题
                item_title = "".join(li.xpath(title))

                # 过滤处理
                result = filter_title(item_title)
                if result == True:
                    continue

                #获取地区
                if li_area != "" :
                    area = "".join(li.xpath(li_area))
                    area = ''.join(re.findall('([\u4e00-\u9fa5])', area))
                else :
                    area = ""

                # 获取项目地址
                href_title = "".join(li.xpath(href))
                href_title = rehref(href_title)

                #域名判断
                if domainName_url != "":
                    href_title = domainName_url + href_title

                # # 获取项目页面中的截止时间等时间信息
                # html_str = self.parse_url(href_title)
                # content_time = regex(html_str)

                # 字典的健为项目标题，值为[项目标题地址,时间]
                if item_title not in self.content_item['招标文件名称']:
                    self.content_item['招标文件名称'].append(item_title)
                    self.content_item['省市区'].append(area)
                    self.content_item['网址'].append(href_title)
                else:
                    continue
                # self.content_item['时间信息'].append(content_time)
                # print('title:{}area:{}href{}time{}'.format(item_title, area, href_title, content_time))
                print('title:{}area:{}href{}'.format(item_title, area, href_title))
                time.sleep(1)
            return True
        except Exception as e:
            print('error: ', e)
            #self.driver.get_screenshot_as_file(r'./error.png')
            return False


    #对全部的标题进行获取
    def ContentAnalysis(self):
        if self.content_item['网址'] != [] :
            href = self.content_item['网址']
            try:
                for i in href:
                    href_title = i
                    # 获取项目页面中的截止时间等时间信息
                    html_str = self.parse_url(href_title)
                    content_time = regex(html_str)
                    #if self.content_item['省市区'][i]=="":
                        #self.content_item['省市区'][i]=content_area
                    self.content_item['时间信息'].append(content_time)
                    time.sleep(random.randint(1, 3))
                return True
            except Exception as e :
                print('error: ', e)
                return False
        else:
            return False
    #取下一页的地址 
    def page_url(self, page_url, page_name, cur_page_num):        
        if page_name["type"]==0:
            page_name = page_name["style"]
            page_split = page_name.split('=')
            pageName = page_split[0]
            next_page = pageName + '=' + str(cur_page_num)
            next_url = re.sub(page_name, next_page, page_url)                
            
        elif page_name["type"]==1:  #中原招采网   Index_count.html
            next_url = page_name["style"].replace(page_name["replaceKey"],str(cur_page_num))
        elif page_name["type"]==2: #河北省招标投标公共服务平台  post请求下一页
            page_name["data"][page_name["pageNoKey"]]=cur_page_num
            next_url = "post"
        elif page_name["type"]==3: #黑龙江政府采购网 
            page_name["onclick"][0]["button"] = page_name["onclick"][0]["button"].replace(page_name["onclick"][0]["replaceKey"],str(cur_page_num))
            next_url = "onclick"
        print("****************************************")
        print("当前运行第{}页".format(cur_page_num))
        print("****************************************")
        return next_url

    #取页的数量
    def number_page(self,number_xpath, page_html_str):
        # 把html字符串转换成element对象
        html_element = etree.HTML(page_html_str)
        number = html_element.xpath(number_xpath)
        return number

    #拼地址(搜索需要地址拼接)
    def Search(self, url, search01):
        query_string = urllib.parse.urlencode(search01)
        print(query_string)
        url += query_string
        print(url)
        return url

    #最后调用,返回结果集
    def result(self):
        # 创建存储信息的列表
        return self.content_item

    #关闭驱动
    def quit(self):
        self.driver.quit()