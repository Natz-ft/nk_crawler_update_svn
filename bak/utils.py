#-*- coding:utf-8 -*-
import threading
from io import BytesIO
from telnetlib import EC

from PIL import Image
from selenium.webdriver.common.by import By

from config import include_keys, exclude_keys, area_dict,area_list
from fake_useragent import UserAgent
import re
import requests
import time
import random
import area
import datetime
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC

headers = {"User-Agent": UserAgent().chrome}

def parse_url(href_title, headers=headers,cookie_dict=None, driver=''):
    """
   采用request或selenuim方法，解析网址，返回html字符串
    :param href_title:
    :return:
    """
    if driver == '':
        # 发送request请求
        response = requests.get(href_title, headers=headers,cookies=cookie_dict)
        time.sleep(random.randint(1, 3))
        print("response:", response)
        #html_str = unescape(response.text)
        html_str = response.content.decode()
    else:
        driver.get(href_title)
        time.sleep(random.randint(1, 3))
        html_str = driver.page_source
    return html_str



def filter_title(title):
    '''
    过滤标题：将有含关键字，不含剔除关键的标题返回False，否则返回True，将标题过滤
    :param title:
    :return:
    '''
    print(title)
    include_pattern = r"(?=(" + '|'.join(include_keys) + r"))"
    exclude_pattern = r"(?=(" + '|'.join(exclude_keys) + r"))"
    r1 = re.findall(include_pattern, title)
    r2 = re.findall(exclude_pattern, title)
    if len(r1) > 0 and len(r2) == 0:
        return False
    else:
        return True       #真的需要过滤

def regex(html_str):
    '''
    返回时间信息，招标文件发布的地点信息，格式为列表
    :param html_str:
    :return:
    '''
    #取出html标签，以便正则匹配文字
    label = r'\r|\t|\n|<strong>|</strong>|<span .*?>|<span>|</span>|<SPAN.*?>|</SPAN>|<FONT.*?>|</FONT>|<a .*?>|<a>|</a>|<div .*?>|<div>|</div>|<table .*?>|<table>|</table>|<tr .*?>|<tr>|</tr>|<td .*?>|<td>|</td>|<p .*?>|<p>|</p>|<SPAN.*?>|</SPAN>|<U.*?>|</U>|<P.*?>|</P>|<TD.*?>|</TD>|<TR.*?>|</TR>|<TBODY.*?>|</TBODY>|<TABLE.*?>|</TABLE>|<DIV.*?>|</DIV>'
    html_str = re.sub(label, "", html_str)
    html_str = re.sub(' ', "", html_str)
    #时间信息正则
    pattern_t = re.compile(r'([\u4e00-\u9fa5]{1,13}：*[\u4e00-\u9fa5]*\d{4}[-,年]\d{1,2}[-，月]\d{1,2})')
    #地点信息正则
    pattern_a = re.compile(r'地点.*?： *[\u4e00-\u9fa5]{1,10}')
    content_time, content_area = pattern_t.findall(html_str), "".join(pattern_a.findall(html_str))
    content_area_new = getAreaFromStr(content_area)
    if content_area_new == "":
        content_area_new = "中国"
    return content_time, content_area_new

def search_area(content):
    pattern = r"(?=(" + '|'.join(area_list) + r"))"
    area = "".join(re.findall(pattern, content))
    return area

def area_tpye(area):
    """
    判断区域类型：
    输入区域，返回区域所在省份，如果找不到，返回“中国”
    :param area:
    :return:
    """
    for k in area_dict.keys():       #遍历字典keys（省份），如果区域在key里找到，返回省份
        if str(area) in k:
            return k
    for k, v in area_dict.items():   #遍历values（省份所在区域），返回归属省份
        for e in v:
            if area in e:
                return k
    return "中国"                    #没找到，返回中国，方便调试观察



#获取详细信息地址
def rehref(href_title):
    """
    正则获取 href 地址信息
    href_title：xpath 获取到的带有连接信息的字符串
    """
    #javascript:urlOpen('url')
    #javascript:location.href='url';return false;
    href_arr = re.findall(r'[\'](.*?)[\']',href_title)
    if len(href_arr)==1:
        href = href_arr[0]
    elif len(href_arr)>1:
        #showProjectDetail('014002007','9990000000010328373');
        href = "/".join(href_arr)
    else:
        #goNewPage(64283,7);   http://www.cpeinet.com.cn/cpcec/bul/bul_show.jsp?id=64283
        href_tmp = "".join(re.findall(r'[\(](.*?)[\)]',href_title))
        if len(href_tmp) and ',' in href_tmp:
            href = href_tmp.split(',')[0]
        else:
            href = href_title
        
    # 去除 第一个.
    href = re.sub(r'^[\.]',"",href)    
    return href

#获取总的页数
def retotalPage(ori_number):
    if len(ori_number)==0:
        return 0

    # 分页按钮不固定的 获取1，2，3，4，....列表  取最大值
    if len(ori_number)>1:
        num_list = list(filter(lambda x: x.isdigit(), ori_number))
        if len(num_list)>0:
            number = max(num_list)
            return number
    
    number = ''.join(re.findall(r'\d+页', ''.join(ori_number))).replace("页","")
    if len(number)==0:
        number = max(re.findall(r'\d+', ''.join(ori_number)))

    return number

#获取；匹配地址
def getAreaFromStr(title):
    #提取汉字
    pat=re.compile(r'[\u4e00-\u9fa5]+')
    title="".join(pat.findall(title)) 
       
    #title = re.sub(r"\(.*?\)|\（.*?\）", "", title)
    #title = re.sub('[\(\).*?\（\）]',"",title)
    if "省" in title:
        pattern_t = re.compile(r'([\u4e00-\u9fa5].*?省)')  
    elif "市" in title:
        pattern_t = re.compile(r'([\u4e00-\u9fa5].*?市)') 
    elif "县" in title:
        pattern_t = re.compile(r'([\u4e00-\u9fa5].*?县)')
    else:
        pattern_t = re.compile(r'([\u4e00-\u9fa5]{1,22})')
    
    title_str = "".join(pattern_t.findall(title))
    if len(title_str)<4:
        return title_str
    for dif in range(4,1,-1):
        title_str_new = "".join(["(" + title_str[i:i+dif] + ").*?|" for i in range(len(title_str)-1)])
        pattern_n = re.compile(title_str_new)
        tmp_str = pattern_n.findall(area.area_str)
        result = ["".join(tmp) for tmp in tmp_str if len("".join(tmp))!=0]
        if len(result)>0:
            break
    if len(result)!=0:
        result = sorted(result,key=lambda k:len(k),reverse=True)[0]
    else:
        result = ""
    return result


#get请求 请求超时处理
def loopRefresh(driver):
    count = 0
    for i in range(3):
        try:
            driver.refresh()
            break
        except:
            count = count+1
            pass
    if count ==3:
        return False
    else:
        return True
    
    
#千里马;中国采招网：吉林
def  isLogin_byXpath(driver,xpathStr):
    try:
        pop_windows = driver.find_element_by_xpath(xpathStr)
        return False
    except:
        return True
    
# 将标题时间转化为 xxxx-xx-xx 字符串格式
def getTitleTimeStr(stime):
    # xxxx年xx月xx日
    p = re.compile('(\d{4})[年，-](\d{1,2})[月,-](\d{1,2})')
    submit_time = p.findall(stime)
    if len(submit_time):
        submit_time = "-".join(submit_time[0])
        return submit_time
    # xx月xx日
    p = re.compile('(\d{1,2})[月,-](\d{1,2})')    
    submit_time = p.findall(stime)
    if len(submit_time):
        year = datetime.datetime.now().year
        submit_time = str(year)+"-"+"-".join(submit_time[0])
        return submit_time
    # xxxx/xx/xx
    p = re.compile('(\d{4})[/](\d{1,2})[/](\d{1,2})')
    submit_time = p.findall(stime)
    if len(submit_time):
        submit_time = "-".join(submit_time[0])
        return submit_time  
    # xxxx.xx.xx
    p = re.compile('(\d{4})[.](\d{1,2})[.](\d{1,2})')
    submit_time = p.findall(stime)
    if len(submit_time):
        submit_time = "-".join(submit_time[0])
        return submit_time     
        
    return ""

def get_track(distance):
    """
    根据偏移量获取移动轨迹
    :param distance: 偏移量
    :return: 移动轨迹
    """
    # 移动轨迹
    track = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 计算间隔
    t = 0.2
    # 初速度
    v = 0

    while current < distance:
        if current < mid:
            # 加速度为正 2
            a = 4
        else:
            # 加速度为负 3
            a = -3
        # 初速度 v0
        v0 = v
        # 当前速度 v = v0 + at
        v = v0 + a * t
        # 移动距离 x = v0t + 1/2 * a * t^2
        move = v0 * t + 1 / 2 * a * t * t
        # 当前位移
        current += move
        # 加入轨迹
        track.append(round(move))
    return track
def move_to_gap(browser,slider, tracks):
    """
    拖动滑块到缺口处
    :param slider: 滑块
    :param tracks: 轨迹
    :return:
    """
    ActionChains(browser).click_and_hold(slider).perform()
    for x in tracks:
        ActionChains(browser).move_by_offset(xoffset=x, yoffset=0).perform()
    time.sleep(0.5)
    ActionChains(browser).release().perform()
def scrollVerify(driver,moveElementXPath,distance):
    track_list = get_track(distance)
    #import random
    #track_list = []
    #num = distance//50
    #track_list = [50]*num
    #if distance%50>0:
        #track_list.append(distance%50)
    moveElement = driver.find_element_by_xpath(moveElementXPath)
    #鼠标点击元素并按住不放
    ActionChains(driver).click_and_hold(on_element=moveElement).perform()
    track_sum = 0
    for i, track in enumerate(track_list):
        #track_sum = track_sum+track
        #print(track_sum)
        #拖动元素
        ActionChains(driver).move_to_element_with_offset(to_element=moveElement, xoffset=track, yoffset=0).perform()
        #if i <num:
            #time.sleep(random.randint(10,50)/100)
    #ActionChains(driver).release(on_element=moveElement).perform()
    ##释放元素
    #ActionChains(driver).release(on_element=moveElement).perform()
    pass


############################zl 粘贴 手动输入验证码####################################
    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        return (top, bottom, left, right)

    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_geetest_image(self, name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        img = Image.open('./captcha.png')
        img_thread = threading.Thread(target=img.show, daemon=True)
        img_thread.start()
        capt = input('请输入图片里的验证码：')
        re

##################################################################################


#if __name__ == '__main__':
    ###from CrawlerModule import Init_driver
    ###driver = Init_driver()
    ###driver.get("https://jl.bidcenter.com.cn/diqumore-1-6.html")
    ###moveElementXPath = "//span[@id='nc_1_n1z']"
    ###distance = 258
    ####scrollVerify(driver, moveElementXPath, distance)  