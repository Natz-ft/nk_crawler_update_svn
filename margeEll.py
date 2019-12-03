# -*- coding:utf-8 -*-
import os
import re

import xlrd
import requests
from lxml import etree
from selenium import webdriver
import time

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
        }

def margeEllipsis(fileDir,newDir):
    xlsDirs = []
    fileNames = []
    for home, dirs, files in os.walk(fileDir):
        for fileName in files:
            fileNames.append(os.path.splitext(fileName)[0])
            fullName = os.path.join(home, fileName)
            xlsDirs.append(fullName)
    for i in range(len(xlsDirs)):
        xlsDir = xlsDirs[i]
        with open(newDir + fileNames[i] + '.txt','w') as wr:
            xlsBefore = xlrd.open_workbook(xlsDir)
            sheet1 = xlsBefore.sheet_by_index(0)
            for index in range(1,sheet1.nrows):
                cell_value = sheet1.cell(index,1).value
                if cell_value.find('...') != -1:
                    url = sheet1.cell(index,3).value
                    try:
                        new_value = getFull(url,cell_value,requests.get(url=url,headers=headers).text)
                        print(new_value)
                        if new_value != None:
                            wr.write(new_value)
                        else:
                            wr.write(cell_value)
                    except:
                        wr.write(cell_value)
                    wr.write('\n')
def getFull(url,cell,res):
    fullTitle = cell
    try:
        if url.find('cfcpn.com') != -1:
            ele = etree.HTML(res)
            more = ele.xpath('/html/body/div[4]/div/div[2]/div[1]/div[1]/p[1]/text()')
            if more:
                fullTitle = more[0]
            else:
                more = ele.xpath('//[@id="news_head"]/p[1]/text()')
                if more:
                    fullTitle = more[0]
                else:
                    fullTitle = cell
        elif url.find('b2b.10086.cn') != -1:
            ele = etree.HTML(res)
            fullTitle = ele.xpath('/html/body/div/div[1]/table/tr[2]/td/h1/text()')[0]
        elif url.find('ccgp-beijing.gov.cn') != -1:
            ele = etree.HTML(res)
            fullTitle = ele.xpath('/html/body/div[2]/div[2]/span/text()')[0]
        elif url.find('ccgp-jiangsu.gov.cn ') != -1:
            ele = etree.HTML(res)
            fullTitle = ele.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/h1/text()')[0].strip()
        elif url.find('gc-zb.com') != -1:
            ele = etree.HTML(res)
            try:
                title = ele.xpath('/html/body/div/div[4]/div[2]/div[1]/h1/text()')[0].split('...')[0]
                title_index = title.find(']')
                if title_index != -1:
                    title_key = title[0:title_index+1]
                    title_end = ele.xpath('//div[@class="read_content"]/table/tbody/tr/td/table/tbody/tr/td/b/text()')[0].strip().split('的')[1]
                    if ele.xpath('//*[@id="Table1"]/tbody/tr[2]/td[4]/text()'):
                        title_mid = ele.xpath('//*[@id="Table1"]/tbody/tr[2]/td[4]/text()')[0].strip() + \
                                    ele.xpath('//*[@id="Table1"]/tbody/tr[3]/td[4]/text()')[0].strip()
                    else:
                        title_mid = ele.xpath('//*[@id="Table1"]/tbody/tr[3]/td[2]/text()')[0].strip() + \
                                    ele.xpath('//*[@id="Tr2"]/td[2]/text()')[0].strip()
                        if not title_mid:
                            title_full = ele.xpath('//h1[@class="con_title"]/text()')[0]
                            return title_full
                    title_full = title_key + title_mid + '的' + title_end
                else:
                    title_full = ele.xpath('//div[@class="read_content"]/div/div/p[1]//b/text()')
                    title_full = "".join(title_full)
                    if title_full != "":
                        fullTitle = title_full
                        return fullTitle
                    else:
                        title_full = ele.xpath('//h1[@class="con_title"]/text()')[0]
            except:
                title_full = ele.xpath('//h1[@class="con_title"]/text()')[0]
            fullTitle = title_full
    except:
        fullTitle = cell
    return fullTitle


if __name__ == "__main__":
    fileDir = "C:\\Users\\75734\\Desktop\\data\\data"
    margeDir = 'C:\\Users\\75734\\Desktop\\data\\marge\\'
    margeEllipsis(fileDir,margeDir)
