# -*- coding:utf-8 -*-
# Author:toby
# Date : 2021/12/20 14:08
import time

from selenium import webdriver
dr = webdriver.Chrome()  # 调用谷歌浏览器
dr.maximize_window()  # 最大化浏览器
dr.get("https://www.facebook.com/")  # 通过get()方法，打开一个url站点
time.sleep(2)
dr.find_element_by_id('email').send_keys('1712754006@qq.com')
time.sleep(2)
dr.find_element_by_id('pass').send_keys('binglu30+du')
dr.find_element_by_css_selector("[name='login']").click()