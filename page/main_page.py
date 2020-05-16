# -*- coding: utf-8 -*-
# @Author  : Bruce.Chen
# @Time    : 2020/5/16 12:06
# @File    : main_page.py
# @Software: PyCharm
from appium.webdriver.webdriver import WebDriver

from page.search_page import SearchPage


class MainPage(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def to_search(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        return SearchPage(self.driver)