# -*- coding: utf-8 -*-
# @Author  : Bruce.Chen
# @Time    : 2020/5/16 3:54
# @File    : app.py
# @Software: PyCharm
from appium import webdriver
from driver.driver_info import *
from page.main_page import MainPage


class App:

    def __init__(self):
        self.driver = webdriver.Remote(AppiumServerUrl, VirtualConnection)
        self.driver.implicitly_wait(10)

    def start(self):
        return MainPage(self.driver)

    def quit(self):
        self.driver.quit()
