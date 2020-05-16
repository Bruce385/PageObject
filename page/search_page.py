# -*- coding: utf-8 -*-
# @Author  : Bruce.Chen
# @Time    : 2020/5/16 12:13
# @File    : search_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class SearchPage(BasePage):
    _input_locator = (By.ID, "com.xueqiu.android:id/search_input_text")
    _name_locator = (By.ID, "com.xueqiu.android:id/name")

    def search_po(self, keyword):
        self.find_element(self._input_locator).send_keys(keyword)
        self.find_element(self._name_locator).click()

    def get_current_price(self):
        return float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
