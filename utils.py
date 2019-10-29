#-*- coding:utf-8 -*-
import datetime

from config import include_keys, exclude_keys, area_dict,area_list
from fake_useragent import UserAgent
import re
import requests
import time
import random
import area
import datetime

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
    href_tmp = "".join(re.findall(r'[\'](.*?)[\']',href_title))
    if len(href_tmp)>0:
        href = href_tmp
    else:
        href = href_title
    return href

#获取总的页数
def retotalPage(ori_number):
    # 分页按钮不固定的 获取1，2，3，4，....列表  取最大值
    if len(ori_number)>1:
        number = max(list(filter(lambda x: x.isdigit(), ori_number)))
    else:
        # 
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
    p = re.compile('(\d{4})[年，-](\d{1,2})[月,-](\d{1,2})')
    submit_time = p.findall(stime)
    if len(submit_time)==0:
        #月日
        p = re.compile('(\d{1,2})[月,-](\d{1,2})')
        submit_time = p.findall(stime)
        if len(submit_time):
            year = datetime.datetime.now().year
            submit_time = str(year)+"-"+"-".join(submit_time[0])
        else:
            submit_time=""
    else:
        #年月日
        submit_time = "-".join(submit_time[0])
    return submit_time



if __name__ == '__main__':
    #str1 = '地点开标时间：2019-10-0909:30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;开标地点：北京经济技术开发区地'
    #a = search_area(str1)
    #print(a)
    tmp = "中共黑龙江省直属机关工作委员会_办公设备_SC[2019]5212网上竞价公告"
    tmp = '地点、方式及招标文件售价：(1)凡有意参加投标者，请于2019年10月24日起至2019年10月31日，每日上午09:00时到12:00时，下午14：30时到17:00时(北京时间，节假日除外)在招标代理机构&nbsp;华新项目管理集团有限公司(地址：长沙市天心区保利国际地点：6.1投标截止：2019年11月20日9:00时止，超过截止时间的投标将被拒绝（☆）。6.2开标时间：2019年11月20日9:00时。6.3开标地点（递交投标文件地点）：华新项目管理集团有限'
    result = getAreaFromStr(tmp)
    print(result)