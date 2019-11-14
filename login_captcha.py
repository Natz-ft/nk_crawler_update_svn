# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:50:14 2019

@author: 16703
"""
import math
from selenium import webdriver
from PIL import Image
import time
import cv2
import os
import sys
sys.path.append(os.path.abspath("./model"))
from model.pred import captcha_1_pred

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class Loop():
    #初始化url;启动web_driver
    def __init__(self,url):      
        self.temp_url = url
        self.driver = webdriver.Chrome('chromedriver.exe')
    
    def get_img(self,drivers,imgxpath):
        driver.get(self.temp_url)
        img = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, imgxpath)))
        driver.save_screenshot(r'./code_full.png')#截图
        
        location = img.location
        size = img.size        
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        login_img = cv2.imread('./code_full.png')
        #截图
        cut_image = login_img[top:bottom,left:right] 
        return cut_image
        
    def get_char(self,driver,imgxpath,num_left=0,num_top=0):
        driver.get(self.temp_url)
        time.sleep(5)
        driver.save_screenshot(r'./code_full.png')#截图
        href=driver.find_element_by_xpath(imgxpath) #获取验证码坐标
        login_img = cv2.imread('./code_full.png')
        login_height,login_width = login_img.shape[:2]
        size_window = driver.get_window_size()
        #计算浏览器与截图比例
        scale = size_window['width'] / login_width
        #获取验证码位置，根据前端调整 + number
        location_X = math.ceil(href.location['x'] / scale) + num_left
        location_Y = math.ceil(href.location['y'] / scale) + num_top
        location_height = math.ceil(href.size['height'] / scale)
        location_width = math.ceil(href.size['width'] / scale)
        #截图
        cut_image = login_img[location_Y:location_Y + location_height,location_X:location_X + location_width]
        return cut_image

        #picture.save('./captcha_img.jpg')
if __name__ == '__main__':
    url = 'http://liaoning.bidchance.com/tspt_210000_0_02_0_1.html'
    loop = Loop(url)
    #cut_image = loop.get_char(loop.driver,'//*[@id="randimg"]',5)
    cut_image = loop.get_img(loop.driver,'//*[@id="randimg"]')
    cv2.imshow("cut_image",cut_image);cv2.waitKey(0)
    from tensorflow.keras.models import load_model
    model = load_model(os.path.abspath("./model/model_1.h5"))
    res = captcha_1_pred(cut_image,model)
    print(res)
    
