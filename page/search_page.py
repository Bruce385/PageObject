# -*- coding: utf-8 -*-
# @Author  : Bruce.Chen
# @Time    : 2020/5/16 12:13
# @File    : search_page.py
# @Software: PyCharm
from appium.webdriver.webdriver import WebDriver


class SearchPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def search_po(self, keyword):
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(keyword)
        self.driver.find_element_by_id("com.xueqiu.android:id/name").click()

    def get_current_price(self):
        return self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text
