# -*- coding:utf-8 -*-
# 整合
from mail import Mail
import re
import pandas as pd
from config import config, default, include_keys, information,bank,mailParams
from collections import defaultdict
from logger import Logger
import argparse
import traceback
from test import Test
from test_login import Test_login
from test_loop3 import Test_loop3
from test_json import TestJson
import utils
import time
import os
import sys
from verify_model_predict import Verify_code_predict
from area import area_tpye
import datetime

def parse_args():
    parser = argparse.ArgumentParser(description="config_info")
    parser.add_argument('--start-time', type=str, default=default.start_time, help='default config')
    parser.add_argument('--file-path', type=str, default=default.file_path, help='default config')
    parser.add_argument('--save-path', type=str, default=default.save_path, help='default config')
    #parser.add_argument('--save-filename', type=str, default=default.save_filename, help='default config')
    parser.add_argument('--interactive_file', type=str, default=default.interactive_file, help='default config')
    parser.add_argument('--choice-run', type=str, default=default.choice_run, help='default config')

    args = parser.parse_args()
    return args


log = Logger()
logger = log.logger_Info()


class Focus():
    def __init__(self):
        self.key_array = include_keys

    def time_change(self, df):
        d = defaultdict(list)
        df = pd.DataFrame(df)
        if '时间信息' in df.keys():
            for k, i in enumerate(df['时间信息']):
                # regex = '.*[\u4E00-\u9FA5]{0,10}投标[\u4E00-\u9FA5]{0,10}(\d{4}[年，-]\d{1,2}[月,-]\d{1,2})'
                time_t = []
                time_end = []
                for key in i:
                    if type(key) is list:
                        for item in key:
                            if "截止" in item:
                                time_end.append(item)
                            else:
                                time_t.append(item)
                    elif type(key) is str:
                        if key != '':
                            if "截止" in key:
                                time_end.append(key)
                            else:
                                time_t.append(key)

                regex = '.*?投标.*?(\d{4}[年，-]\d{1,2}[月,-]\d{1,2})'
                p = re.compile(regex)
                stime = p.findall(''.join(time_t))
                if stime != []:
                    d['投标时间'].append(stime[0])
                else:
                    d['投标时间'].append(None)

                regex = '.*?报名.*?(\d{4}[年，-]\d{1,2}[月,-]\d{1,2})'
                p = re.compile(regex)
                stime = p.findall(''.join(time_t))
                if stime != []:
                    d['报名时间'].append(stime[0])
                else:
                    d['报名时间'].append(None)

                # regex = '.*[\u4E00-\u9FA5]{0,10}截止[\u4E00-\u9FA5]{0,10}(\d{4}[年，-]\d{1,2}[月,-]\d{1,2})'
                regex = '.*?投标截止.*?(\d{4}[年，-]\d{1,2}[月,-]\d{1,2})'
                p = re.compile(regex)
                stime = p.findall(','.join(time_end))
                if stime != []:
                    d['截止时间'].append(stime[0])
                else:
                    d['截止时间'].append(None)
            df = df.drop(columns=['时间信息'])
            d = pd.DataFrame(d)
            d = d.reset_index(drop=True)
            df = df.reset_index(drop=True)
            frames = [df, d]
            result = pd.concat(frames, axis=1)
            if 'Unnamed: 0' in result.keys():
                result = result.drop(columns=['Unnamed: 0'])
            return result
    #增加两列
    def bank(self, text,type_str): 
        #将所有银行名称写正则表达式
        df = pd.DataFrame(text)
        d = defaultdict(list)
        str_text = ""
        #拼接正则表达式
        for i in bank:
            str_text = str_text + ".*?("  + i + ").*?" + "|"
        str_text = str_text[0:len(str_text)-1]
        pattern_t = re.compile(str_text)        
        if '招标文件名称' in df.keys():
            for k, i in enumerate(df['招标文件名称']):
                if type_str!="":
                    d['类型'].append(type_str)
                elif "中标" in i:
                    d['类型'].append("中标")
                else:
                    d['类型'].append("招标")
                content_bank = pattern_t.findall(i)
                if content_bank != [] :
                    te = "".join(list(content_bank[0]))
                    d['银行全称'].append(str(te))
                    if "分行" in i:
                        d['行别'].append("分行")
                    elif "支行" in i :
                        d['行别'].append("分行")
                    else :
                        d['行别'].append("总行")
                else :
                    d['银行全称'].append("")
                    d['行别'].append("")
        print(d)
        d = pd.DataFrame(d)
        d = d.reset_index(drop=True)
        df = df.reset_index(drop=True)
        frames = [df, d]
        result = pd.concat(frames, axis=1)
        if 'Unnamed: 0' in result.keys():
            result = result.drop(columns=['Unnamed: 0'])  
        return result
    def Pipeline(self, key,vericode):
        try:
            text = information[key]
            csv = default.file_path + "/" + text["csv"]
            # 实例化对象
            print(text["classname"])
            testClass = globals()[text["classname"]]()
            # 运行程序
            result = testClass.RunMain(text["original_url"], self.key_array, key,vericode)
            result = self.bank(result,text["type"])
            pd.DataFrame(self.time_change(result)).to_csv(csv, encoding='utf_8_sig')
            sum = 0
            res = pd.DataFrame({})
            if type(res) == type(result):
                if result.empty != True:
                    sum = len(result["招标文件名称"])
            elif result != None:
                sum = len(result["招标文件名称"])
            logger.info("运行成功: " + str(key) + ", 一共：" + str(sum) + "条")

        except:
            logger.error("运行失败: " + str(key))
            logger.error(traceback.format_exc())
            # logger.exception("Exception Logged")

    # 动态调用网址
    def find_all(self):
        vericode = Verify_code_predict()
        print("--------------------------------------------程序开始--------------------------------------------")
        for i, key in enumerate(information):
            self.Pipeline(key,vericode)
        print("--------------------------------------------程序结束--------------------------------------------")

    def format_date(self, time):
        res = re.findall('(\d{4})\D(\d{0,2})\D(\d{0,2})', time)[0]
        year = res[0]
        month = res[1]
        date = res[2]
        if len(month) == 1:
            month = '0' + month
        if len(date) == 1:
            date = '0' + date
        time = year + "年" + month + "月" + date + "日"
        return time
def format_date(time):
    res = re.findall('(\d{4})\D(\d{0,2})\D(\d{0,2})', time)[0]
    year = res[0]
    month = res[1]
    date = res[2]
    if len(month) == 1:
        month = '0' + month
    if len(date) == 1:
        date = '0' + date
    time = year + "年" + month + "月" + date + "日"
    return time

if __name__ == "__main__":
    startTime = time.time()
    focus = Focus()
    focus.find_all()
    rangeTime = time.time()-startTime
    print("cost total time is {}".format(rangeTime))
    
    args = parse_args()
    while True:
        current_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
        if current_time == args.start_time: 
            startTime = time.time()
            # 执行爬虫代码
            focus = Focus()
            focus.find_all()
            
            #添加省市区信息
            file_list = os.listdir(args.file_path)
            print(file_list)
            df1 = pd.read_csv(args.file_path + '/' + file_list[0], encoding='utf_8_sig')  # 读取首个csv文件，保存到df1中
            for file in file_list[1:]:
                df_next = pd.read_csv(args.file_path + '/' + file, encoding='utf_8_sig')  # 打开csv文件，注意编码问题，保存到df2中
                df1 = pd.concat([df1, df_next], axis=0, ignore_index=True, sort=False)  # 将df2数据与df1合并
            df1 = df1.drop_duplicates()  # 去重
            # df1['网址'] = '=HYPERLINK("'+df1['网址']+'")'
            for i, v in enumerate(df1['省市区']):
                df1['省市区'][i] = area_tpye(str(v))
            #格式化时间信息为 xxxx年xx月xx日
            current_year = time.strftime('%Y', time.localtime(time.time()))
            for k in ['投标时间', '报名时间', '截止时间']:
                for i, v in enumerate(df1[k]):
                    str_v = str(v)
                    if str_v != "nan":
                        if str_v < current_year:
                            df1[k][i] = None
                        else:
                            df1[k][i] = format_date(str_v)
        
            df1 = df1.reset_index(drop=True)  # 重新生成index
        
            #保存昨天xlsx
            today = datetime.date.today()
            yesterday = str(today - datetime.timedelta(days=1))
            save_filename = args.save_path + '/'+'result_merge' + "_" + yesterday+ '.xls'
            df1.to_excel(save_filename, index=False)  # 将结果保存为新的csv文
        
        
            rangeTime = time.time()-startTime
            print("cost total time is {}".format(rangeTime))
            
            mail = Mail(smtp_server=mailParams.smtp_host_server,
                                username=mailParams.usr_name,
                                password=mailParams.passwd,
                                    from_addr=mailParams.from_addr,
                                    to_addr=mailParams.to_addr,
                                    cc_addr=mailParams.cc_addr,
                                    subject = mailParams.subject,
                                    content = mailParams.content,
                                    attach_file=save_filename)
            mail.send_email()            
