#-*- coding:utf-8 -*-
from config import include_keys, exclude_keys, area_dict,area_list
from fake_useragent import UserAgent
import re
import requests
import time
import random

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
    return content_time, content_area

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
    


if __name__ == '__main__':
    str1 = '地点开标时间：2019-10-0909:30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;开标地点：北京经济技术开发区地'
    a = search_area(str1)
    print(a)
