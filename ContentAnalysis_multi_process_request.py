# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 13:22:02 2019

@author: rcx
"""
import time
import random
import traceback

from multiprocessing import Process, Queue,Manager

import utils

from CrawlerModule import parse_url_request


#对全部的标题进行获取
def ContentAnalysis(model,login_infos,max_process = 4,time_verbose= 0 ):
    if time_verbose:
        time1 = time.clock()
        resContentAnalysis = _ContentAnalysis(model,login_infos,max_process = max_process)
        time_cost = time.clock() - time1
        print('ContentAnalysis timecost: {} s'.format(time_cost))
        return resContentAnalysis
    else:
        return _ContentAnalysis(model,login_infos,max_process = max_process)

def _ContentAnalysis(model,login_infos,max_process = 4,time_verbose= 0 ):
    login_infos = []
    if model.content_item['网址'] != [] :
        try:
            href = model.content_item['网址']

            href_titles_and_drivers = []

            href_title_index_map = {}
            for href_title_index,href_title in enumerate(href):
                href_title_index_map[href_title] = href_title_index
                href_titles_and_drivers.append(href_title)
                
            other_argvs = [model.headers,model.cookie_dict]
                
            model.content_item['时间信息'] = [[]] * len(href)
                
            func_parse_url = parse_url_request; #model.parse_url
            func_utils_regex = utils.regex
            
            results = multi_process_func(func_parse_url,func_utils_regex,
                                         href_titles_and_drivers,other_argvs,max_process= max_process)
            for href_title,content_time, content_area in results:
                href_title_index = href_title_index_map[href_title]
                model.content_item['时间信息'][href_title_index] = content_time
                
            return True
        
        except:
            print('ContentAnalysis error: ')
            traceback.print_exc() #return None
            return False
        
    else:
        return False


def loop(func_parse_url,func_utils_regex,lock,queue,i,results,other_argvs):
    with lock:
        print('process  {}  started...'.format(i))
        
    headers,cookie_dict = other_argvs
    
   
    while 1:      
        href_title = queue.get()
        if href_title == -1:
            queue.put(-1)
            break

        try:           
            html_str = func_parse_url(href_title,headers,cookie_dict,lock,i)        
            content_time, content_area = func_utils_regex(html_str)
            results.append((href_title,content_time,content_area))
            time.sleep(random.randint(1,3))
        except:
            with lock:
                print()
                print('{} {} Error'.format(i,href_title))
                print(traceback.format_exc()) #return str  
            
    with lock:
        print('process  {}  exit...'.format(i))
        
        
        
        

def multi_process_func(func_parse_url,func_utils_regex,href_titles_and_drivers,other_argvs,max_process=4,maxsize_num = 100000):
    '''
    多进程
    ''' 
    queue_job = Queue(maxsize = maxsize_num + 1) ## 1: put(-1)
    for href_title_and_driver in href_titles_and_drivers:
        queue_job.put(href_title_and_driver)
    queue_job.put(-1)
    
    
    manager = Manager()    
    
    lock = manager.Lock()
    process_list = []
    PID =[]
    results = manager.list([])
          
    for i in range(max_process):  ##max_process最大进程数, i:进程编号
        process_parse = Process(target = loop,args = (func_parse_url,func_utils_regex,lock,queue_job,i,results,other_argvs))
        process_parse.start()
        process_list.append(process_parse)
        PID.append(str(process_parse.pid))
    
    for process_parse in process_list:
        process_parse.join()
    
    return results





