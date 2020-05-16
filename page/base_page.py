# -*- coding: utf-8 -*-
# @Author  : Bruce.Chen
# @Time    : 2020/5/16 15:12
# @File    : base_page.py
# @Software: PyCharm
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _black_list = [(By.ID, "image_cancel"), (By.ID, "tv_agree")]

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator):
        try:
            return self.driver.find_element(*locator)
        except:
            self.cancel_window()
            return self.driver.find_element(*locator)

    def cancel_window(self):
        for locator in self._black_list:
            if len(self.driver.find_elements(*locator)) > 0:
                self.driver.find_element(*locator).click()
            else:
                print("%s not found" % str(locator))
