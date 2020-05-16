# -*- coding: utf-8 -*-
# @Author  : Bruce.Chen
# @Time    : 2020/5/16 3:54
# @File    : app.py
# @Software: PyCharm
from appium import webdriver
from driver.driver_info import *
from page.main_page import MainPage


class App:
    @classmethod
    def __init__(cls):
        cls.driver = webdriver.Remote(AppiumServerUrl, VirtualConnection)
        cls.driver.implicitly_wait(10)

    @classmethod
    def start(cls):
        return MainPage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()
