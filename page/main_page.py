# -*- coding: utf-8 -*-
# @Author  : Bruce.Chen
# @Time    : 2020/5/16 12:06
# @File    : main_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.search_page import SearchPage


class MainPage(BasePage):
    _search_locator = (By.ID, "com.xueqiu.android:id/tv_search")

    def to_search_page(self):
        self.find_element(self._search_locator).click()
        return SearchPage(self.driver)
