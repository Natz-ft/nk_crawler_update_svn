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
from importlib import reload
import config
#from config import config
import utils
import urllib.request
import urllib.parse
import requests
requests.packages.urllib3.disable_warnings()
import traceback
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import cv2
import math
import numpy as np
from verify_model_predict import getVerifyCode_func 
import os
from timeout_check import send_timeout_signal,end_timeout_signal
#import psutil    
def Init_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--allow-file-access-from-files")
    chrome_options.add_argument('--headless')#服务器上不注释
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.addArguments("--disable-dev-shm-usage")
    chrome_options.add_argument("window-size=1366x768")
    platform_info = platform.platform()
    platform_info = ''.join(re.findall(r'Windows', platform_info))

    if platform_info == "Windows":
        driver = webdriver.Chrome(config.config.driver_windows, chrome_options=chrome_options)
    else:
        driver = webdriver.Chrome(config.config.driver_linux, options=chrome_options) 
    print("driver init end")
    return driver

def requestsGetByTime(page_url,headers,cookie_dict,timeout=30):
    timeout = config.timeout
    int_by_timeout = 0
    textname = send_timeout_signal(timeout)
    try:  
        if cookie_dict:
            response = requests.get(page_url, headers=headers,cookies=cookie_dict)
        else:
            response = requests.get(page_url,headers={"User-Agent": UserAgent().chrome}) 
    except KeyboardInterrupt:
        print('Interrupt by timeout_check or Ctrl + C')
        int_by_timeout = 1
    finally:
        end_timeout_signal(textname)    
    if int_by_timeout == 1:
        return None
    return response
    


def driverGetBytime(driver,url,timeout=30):
    timeout = config.timeout
    try:   
        get_times = 3
        
        while get_times:
            int_by_timeout = 0
            textname = send_timeout_signal(timeout)
            try:  
                #time.sleep(2)
                driver.get(url)
            except KeyboardInterrupt:
                print('Interrupt by timeout_check or Ctrl + C')
                int_by_timeout = 1
            finally:
                end_timeout_signal(textname)
            
            if int_by_timeout:
                get_times -= 1
            else:
                break
        if int_by_timeout == 1:
            return False
        
    except:
        flag = utils.loopRefresh(driver)
        if not flag:
            return False
    return True

def parse_url_request(page_url,headers,cookie_dict,lock,i):
    response = requestsGetByTime(page_url, headers, cookie_dict)
    if not response:
        print("parse_url_request  get error")
        return ""
    status = response.status_code
    with lock:
        print("{} status_code {}".format(i,status))
    time.sleep(3)
    try:
        html_str = response.content.decode("utf-8")
    except:
        html_str = response.text
    return html_str


# 得到html字符串 子进程专用
def parse_url_get(driver,href_title,waitFocName): #url_type == 'get'
    if not driverGetBytime(driver, href_title):
        print("parse_url_get  get error")
        return ""
    if waitFocName:
        waitFocName(driver)
    time.sleep(3)
    html_str = driver.page_source
    return html_str


# 登陆浏览器 子进程专用
def model_log_in_web(driver,url, login_info,vericode=None):
    if not driverGetBytime(driver, url):
        print("model_log_in_web  get error")
        return driver
    time.sleep(5)
    try:
        params = login_info["params"]
        for param in params:
            if param["type"]=="id":
                WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, param["name"])))
                driver.find_element_by_id(param["name"]).click()
                driver.find_element_by_id(param["name"]).send_keys(param["value"])
            elif param["type"]=="class":
                WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, param["name"])))
                driver.find_element_by_class_name(param["name"]).click()
                driver.find_element_by_class_name(param["name"]).send_keys(param["value"])
            elif param["type"]=="xpath":
                WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, param["name"])))
                driver.find_element_by_xpath(param["name"]).click()
                driver.find_element_by_xpath(param["name"]).send_keys(param["value"])
        if login_info["isHasVerify_code"]:
            flag =True
            if "imgisAllexits" in login_info.keys():
                if not login_info["imgisAllexits"]:
                    try:
                        driver.find_element_by_xpath(verifyParam["imgxPath"])
                    except:
                        flag = False
            if flag:
                WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, login_info["imgxPath"])))
                cutImg = getVerifyCodeImg(driver,login_info)
                
                #cutImg = getVerifyCodeImg_2(driver,login_info)
                if vericode != None:
                    res = vericode.getVerifyCode(cutImg,login_info["modelname"])
                    driver.find_element_by_xpath(login_info["verifyCodexpath"]).send_keys(res)   
                else:
                    res = getVerifyCode_func(cutImg,login_info["modelname"])
                    driver.find_element_by_xpath(login_info["verifyCodexpath"]).send_keys(res)  
                
        driver.find_element_by_xpath(login_info["button"]).click()
        #driver.implicitly_wait(5) 
        time.sleep(5)
    except Exception as e:
        print('model_log_in_web: ', e)
        traceback.print_exc()
    return driver


def getVerifyCodeImg(driver,verifyParam):
    #driver.set_window_size(1349,948)
    time.sleep(1)
    #driver.get(verifyParam["url"])
    #time.sleep(5)
    #driver.save_screenshot(r'./code_full.png')#截图
    
    image = driver.get_screenshot_as_png()
    image = np.asarray(bytearray(image), dtype="uint8")
    login_img = cv2.imdecode(image, cv2.IMREAD_COLOR) 
    
    img = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, verifyParam["imgxPath"]))) #获取验证码坐标
    location = img.location
    size = img.size        
    top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size['width']
    

    cut_image = login_img[top:bottom,left:right]
    #cv2.imwrite("./all.png",login_img)
    #cv2.imwrite("./cutImg.png",cut_image)
    return cut_image

def getVerifyCodeImg_2(driver,verifyParam,num_left=5):
    #driver.save_screenshot(r'./code_full.png')#截图
    time.sleep(1)
    image = driver.get_screenshot_as_png()
    image = np.asarray(bytearray(image), dtype="uint8")
    login_img = cv2.imdecode(image, cv2.IMREAD_COLOR) 
    
    href=driver.find_element_by_xpath(verifyParam["imgxPath"]) #获取验证码坐标
    #login_img = cv2.imread('./code_full.png')
    login_height,login_width = login_img.shape[:2]
    size_window = driver.get_window_size()
    #计算浏览器与截图比例
    scale = size_window['width'] / login_width
    if "num_left" in verifyParam.keys():
        num_left = verifyParam["num_left"]
    #获取验证码位置，根据前端调整 + number
    location_X = math.ceil(href.location['x'] / scale) + num_left
    location_Y = math.ceil(href.location['y'] / scale)
    location_height = math.ceil(href.size['height'] / scale)
    location_width = math.ceil(href.size['width'] / scale)
    #截图
    cut_image = login_img[location_Y:location_Y + location_height,location_X:location_X + location_width]
    return cut_image


def driver_getUrl(driver,url):
    pass

class Crawler_URL:
    def __init__(self):  # 初始化url_array;启动web_drive
        self.headers = {"User-Agent": UserAgent().chrome}
        # 创建存储信息的列表
        self.content_item = defaultdict(list)
        self.cookie_dict = defaultdict(list)
        # 加载chromedriver
        self.driver = Init_driver()
        reload(config)
        self.searchTime = config.searchTime
    
    # 登陆浏览器
    def log_in_web(self,url, login_info,vericode=None):
        self.driver = model_log_in_web(self.driver, url, login_info,vericode)
        #存在 弹出窗口 就 关闭弹出窗口
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass       
        time.sleep(1)
        self.cookie_info = self.driver.get_cookies()                 # 列表中包含多个字典
        self.cookie_dict = {i["name"]: i["value"] for i in self.cookie_info} 
        return self.driver
    # 字符串 通过 requests    
    def parse_url_2(self,pageurl,url_type="get",url_params={},timeout = 30):
        timeout = config.timeout
        int_by_timeout = 0
        textname = send_timeout_signal(timeout)
        try:  
            if url_type == 'get':
                response = requests.session().get(pageurl)
            elif url_type == 'post':
                response = requests.session().post(url_params["post_url"], headers=url_params["headers"], data=url_params["data"])
        except KeyboardInterrupt:
            print('Interrupt by timeout_check or Ctrl + C')
            int_by_timeout = 1
        finally:
            end_timeout_signal(textname)
        if int_by_timeout==1:
            return ""
        time.sleep(1)
        print("response:", response)
        html_str = response.content.decode("utf-8")
        return html_str
        
    # 得到html字符串
    def parse_url(self, href_title,url_type="get",url_params={},timeout= 30):
        timeout = config.timeout
        if url_type=="get":
            if not driverGetBytime(self.driver, href_title):
                return ""
            time.sleep(3)
            html_str = self.driver.page_source
        elif url_type=="post":
            int_by_timeout = 0
            textname = send_timeout_signal(timeout)
            try:  
                response = requests.post(url_params["post_url"], headers=url_params["headers"],  data=url_params["data"])
            except KeyboardInterrupt:
                print('Interrupt by timeout_check or Ctrl + C')
                int_by_timeout = 1
            finally:
                end_timeout_signal(textname)
            if int_by_timeout==1:
                return ""            
            print(response)
            html_str = str(response.content, encoding="utf-8")
        elif url_type=="onclick":
            click_params = url_params["onclick"]
            for url_param in click_params:
                if "url" in url_param.keys():
                    if not driverGetBytime(self.driver, url_param["url"]):
                        return ""
                    time.sleep(5)
                params= url_param["params"]
                if url_param["button"]=="":
                    html_str = self.driver.page_source
                    return html_str
                if len(params)==0:
                    target=self.driver.find_element_by_xpath(url_param["button"])
                    target.location_once_scrolled_into_view
                    #self.driver.execute_script("arguments[0].click();", target)
                    target.click()
                else:
                    for tmp_param in params:
                        if tmp_param["type"]=="id":
                            self.driver.find_element_by_id(tmp_param["name"]).send_keys(tmp_param["value"])
                        elif tmp_param["type"]=="class":
                            self.driver.find_element_by_class_name(tmp_param["name"]).send_keys(tmp_param["value"])
                        elif tmp_param["type"]=="xpath":
                            self.driver.find_elements_by_xpath(tmp_param["name"]).send_keys(tmp_param["value"])
                    self.driver.find_element_by_xpath(url_param["button"]).click()
                time.sleep(3)
            html_str = self.driver.page_source
            #html_str = str(content, encoding="utf-8")
        return html_str
    def get_title_list_2(self,html_str,parame,isloopBytime=True):
        try:
            #获取项目发布时间列表
            pattern = re.compile(parame["li_time"])
            effect_time_list = pattern.findall(html_str)
            
            #获取标题列表
            pattern = re.compile(parame["title"])
            title_list = pattern.findall(html_str) 
            
            #获取ip的id列表
            pattern = re.compile(parame["href"])
            ip_id_list = pattern.findall(html_str)
            
            #获取截至时间列表
            pattern = re.compile(parame["li_endtime"])
            failure_time_list = pattern.findall(html_str)
            
            #获取 地区
            if parame["li_area"] != "" :
                pattern = re.compile(parame["li_area"])
                areas = pattern.findall(html_str)                
            big_count = 0
            equal_count = 0                
            
            for i in range(len(title_list)):
                # 获取项目发布日期
                submit_time = effect_time_list[i]
                
                if isloopBytime:
                    if submit_time > self.searchTime:
                        big_count = big_count+1
                        continue
                    elif submit_time < self.searchTime :
                        continue
                    elif submit_time == self.searchTime:
                        equal_count = equal_count+1                    
                # 获取项目地址
                href_suf = ip_id_list[i] 
                href_title = parame["domainName_url"] + href_suf
                # 获取项目标题
                item_title = title_list[i]
                #过滤处理
                result = utils.filter_title(item_title)
                if result == True:
                    continue
               
                #获取截止时间
                content_time = "截止时间：" + failure_time_list[i]
                
                #获取地区
                if parame["li_area"] != "" :
                    if "省" in areas[i]:
                        pattern_t = re.compile(r'([\u4e00-\u9fa5].*?省)')  
                    elif "市" in areas[i]:
                        pattern_t = re.compile(r'([\u4e00-\u9fa5].*?市)') 
                    elif "县" in areas[i]:
                        pattern_t = re.compile(r'([\u4e00-\u9fa5].*?县)')
                    elif "区" in areas[i]:
                        pattern_t = re.compile(r'([\u4e00-\u9fa5].*?区)')
                    elif "自治州" in areas[i]:
                        pattern_t = re.compile(r'([\u4e00-\u9fa5].*?自治州)')
                    else:
                        pattern_t = re.compile(r'([\u4e00-\u9fa5]+)')
                    
                    area = "".join(pattern_t.findall(areas[i]))
                else :
                    #从标题获取地区
                    area = utils.getAreaFromStr(item_title)
                    
                # 字典的健为项目标题，值为[项目标题地址,时间]
                if item_title not in self.content_item['招标文件名称']:
                    self.content_item['招标文件名称'].append(item_title.replace(" ", ""))
                    self.content_item['省市区'].append(area)
                    self.content_item['网址'].append(href_title)
                    self.content_item['时间信息'].append(content_time)
                else:
                    continue
                print('title:{}area:{}href{}'.format(item_title, area, href_title))
            if isloopBytime:           
                if big_count>0:
                    print("big_count {}".format(big_count))
                    return True
                elif equal_count==0:
                    return False 
            print("equal_count is {}".format(equal_count))
            return True
        except Exception as e:
            print('get_title_list_2 error: ', e)
            traceback.print_exc()
            return False            
    # 4.提取标题（将需要的标题先保存下来）
    def get_title_list(self, page_html_str, parame,isloopBytime=True):
        #get 三次都超时
        if page_html_str == "":
            return False
        li = parame["li"]
        li_time = parame["li_time"]
        title = parame["title"]
        href = parame["href"]
        href_suf = ""
        domainName_url = parame["domainName_url"]
        li_area = parame["li_area"]
        
        if "href_suf" in parame.keys():
            href_suf = parame["href_suf"]
        
        try:
            # 把html字符串转换成element对象
            html_element = etree.HTML(page_html_str)

            big_count = 0
            equal_count = 0            
            
            # 不可以取到 包含所有信息的行
            if li =="":
                titles,hrefs,times,areas = [],[],[],[]
                if li_area != "" :
                    areas = html_element.xpath(li_area)
                titles = html_element.xpath(title)
                hrefs = html_element.xpath(href)
                if li_time !="":
                    times = html_element.xpath(li_time)
                else:
                    isloopBytime = False
                    
                for i in range(len(titles)):                     
                    if isloopBytime:
                        stime = times[i]
                        #时间处理
                        submit_time = utils.getTitleTimeStr(stime)                    
                        
                        #发布的时间不是昨天的时间，就结束本次循环
                        
                        if submit_time > self.searchTime:
                            big_count = big_count+1
                            continue
                        elif submit_time < self.searchTime :
                            continue
                        elif submit_time == self.searchTime:
                            equal_count = equal_count+1
                    # 过滤处理
                    result = utils.filter_title(titles[i])
                    if result == True:
                        continue
                    #获取地区
                    if li_area != "" :
                        if "省" in areas[i]:
                            pattern_t = re.compile(r'([\u4e00-\u9fa5].*?省)')  
                        elif "市" in areas[i]:
                            pattern_t = re.compile(r'([\u4e00-\u9fa5].*?市)') 
                        elif "县" in areas[i]:
                            pattern_t = re.compile(r'([\u4e00-\u9fa5].*?县)')
                        elif "区" in areas[i]:
                            pattern_t = re.compile(r'([\u4e00-\u9fa5].*?区)')
                        elif "自治州" in areas[i]:
                            pattern_t = re.compile(r'([\u4e00-\u9fa5].*?自治州)')
                        else:
                            pattern_t = re.compile(r'([\u4e00-\u9fa5]+)')
                        
                        area = "".join(pattern_t.findall(areas[i]))
                    else :
                        #从标题获取地区
                        area = utils.getAreaFromStr(titles[i])
                    # 获取项目地址
                    href_title = utils.rehref(hrefs[i],domainName_url)
    
                    if href_suf != "":
                        href_title = href_title+href_suf
                    
                    # 字典的健为项目标题，值为[项目标题地址,时间]
                    if titles[i] not in self.content_item['招标文件名称']:
                        self.content_item['招标文件名称'].append(titles[i].replace(" ", ""))
                        self.content_item['省市区'].append(area)
                        self.content_item['网址'].append(href_title)
                    else:
                        continue                        
                    print('title:{}area:{}href{}'.format(titles[i], area, href_title))
                    time.sleep(1)
                if isloopBytime:
                    if big_count>0:
                        return True
                    elif equal_count==0:
                        return False 
                return True
             
             
            #可以取到 包含所有信息的行       
            #行信息
            li_list = html_element.xpath(li)

            #当页面信息为0的时候，结束爬虫
            if len(li_list) == 0:
                next_type = parame["page_name"]["type"]
                # 获取下一页的方式不是post 
                if next_type != 2:
                    try:
                        self.driver.refresh()
                        WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, li)))
                    except:
                        print("get_title_list get the length of li is time out")
                    page_html_str = self.driver.page_source
                    html_element = etree.HTML(page_html_str)
                    li_list = html_element.xpath(li)
                    if len(li_list)==0:
                        print("li_list:", len(li_list))
                        return False
            
            

            # 遍历所有li元素
            for li in li_list[0:]:
                if len(li_time)==0:
                    isloopBytime = False
                else:
                    # 获取项目发布日期
                    stime = "".join(li.xpath(li_time))
    
                    if stime == "":
                        continue

                    #时间处理
                    submit_time = utils.getTitleTimeStr(stime)
                    
                if isloopBytime:              
                    
                    #发布的时间不是昨天的时间，就结束本次循环
                    
                    if submit_time > self.searchTime:
                        big_count = big_count+1
                        continue
                    elif submit_time < self.searchTime :
                        continue
                    elif submit_time == self.searchTime:
                        equal_count = equal_count+1

                # 获取项目标题
                item_title = "".join(li.xpath(title))

                # 过滤处理
                result = utils.filter_title(item_title)
                if result == True:
                    continue

                #获取地区
                if li_area != "" :
                    area = "".join(li.xpath(li_area))
                    area = ''.join(re.findall('([\u4e00-\u9fa5])', area))
                else :
                    #从标题获取地区
                    area = utils.getAreaFromStr(item_title)

                # 获取项目地址
                href_title = "".join(li.xpath(href))
                href_title = utils.rehref(href_title,domainName_url)


                if href_suf != "":
                    href_title = href_title+href_suf                

                # # 获取项目页面中的截止时间等时间信息
                # html_str = self.parse_url(href_title)
                # content_time = regex(html_str)

                # 字典的健为项目标题，值为[项目标题地址,时间]
                if item_title not in self.content_item['招标文件名称']:
                    self.content_item['招标文件名称'].append(item_title.replace(" ", ""))
                    self.content_item['省市区'].append(area)
                    self.content_item['网址'].append(href_title)
                else:
                    continue
                # self.content_item['时间信息'].append(content_time)
                # print('title:{}area:{}href{}time{}'.format(item_title, area, href_title, content_time))
                print('title:{}area:{}href{}'.format(item_title, area, href_title))
                time.sleep(1)
            if isloopBytime:
                if big_count>0:
                    return True
                elif equal_count==0:
                    return False           
            return True
        except Exception as e:
            print('get_title_list error: ', e)
            traceback.print_exc()
            #self.driver.get_screenshot_as_file(r'./error.png')
            return False



    #对全部的标题进行获取
    def ContentAnalysis(self,waitFocName=None):
        startTime = time.time()
        if self.content_item['网址'] != [] :
            href = self.content_item['网址']
            try:
                for i in href:
                    href_title = i
                    # 获取项目页面中的截止时间等时间信息
                    html_str = parse_url_get(self.driver,href_title,waitFocName)
                    content_time, content_area = utils.regex(html_str)
                    #if self.content_item['省市区'][i]=="":
                        #self.content_item['省市区'][i]=content_area
                    self.content_item['时间信息'].append(content_time)
                    time.sleep(random.randint(1, 3))
                endTime = time.time()-startTime
                print("ContentAnalysis total time is {}".format(endTime))
                return True
            except Exception as e :
                print('ContentAnalysis error: ', e)
                traceback.print_exc()
                return False
        else:
            return False   
        
    #取下一页的地址 
    def page_url(self, page_url, page_name, cur_page_num):        
        if page_name["type"]==0:
            page_name = page_name["style"]
            if '=' in page_name:
                page_split = page_name.split('=')
                pageName = page_split[0]
                next_page = pageName + '=' + str(cur_page_num)
                next_url = re.sub(page_name, next_page, page_url) 
            elif '_' in page_name:
                page_split = page_name.split('_')
                pageName = page_split[0]
                next_page = pageName + '_' + str(cur_page_num)
                next_url = re.sub(page_name, next_page, page_url)                
            
        elif page_name["type"]==1:  #中原招采网   Index_count.html
            next_url = page_name["style"].replace(page_name["replaceKey"],str(cur_page_num))
        elif page_name["type"]==2: #河北省招标投标公共服务平台  post请求下一页
            page_name["data"][page_name["pageNoKey"]]=cur_page_num
            next_url = "post"
        elif page_name["type"]==3: #黑龙江政府采购网 
            if page_name["onclick"][0]["replaceKey"]!="":
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
        if html_element is not None:
            number = html_element.xpath(number_xpath)
        else:
            number = []
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
        #driver_process = psutil.Process(driver.service.process.pid)
        #if driver_process.is_running():
            #driver_process.kill()        
        self.driver.quit()