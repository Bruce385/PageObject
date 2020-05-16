# -*- coding: utf-8 -*-
# @Author  : Bruce.Chen
# @Time    : 2020/5/16 3:54
# @File    : app.py
# @Software: PyCharm
from appium import webdriver
from driver.driver_info import *
from page.main_page import MainPage


class App:

    def start(self):
        self.driver = webdriver.Remote(AppiumServerUrl, VirtualConnection)
        self.driver.implicitly_wait(10)
        print("app start")
        return MainPage(self.driver)

    def cancel_window(self):
        if len(self.driver.find_elements_by_xpath(
                "//*[contains(@text, '同意') and contains(@resource-id, 'tv_agree')]")) > 0:
            self.driver.find_element_by_xpath(
                "//*[contains(@text, '同意') and contains(@resource-id, 'tv_agree')]").click()

    def quit(self):
        self.driver.quit()
