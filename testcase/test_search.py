# -*- coding: utf-8 -*-
# @Author  : Bruce.Chen
# @Time    : 2020/5/16 12:17
# @File    : test_search.py
# @Software: PyCharm
import pytest
import yaml

from page.app import App


class TestSearch:

    def setup(self):
        self.search_page = App().start().to_search_page()

    @pytest.mark.parametrize("keyword,expect_price",
                             yaml.load(open('../data/searchdata.yaml', 'r', encoding='utf-8'), Loader=yaml.FullLoader))
    def test_search_page(self, keyword, expect_price):
        self.search_page.search_po(keyword)
        current_price = self.search_page.get_current_price()
        print("%d >= %d" % (current_price, expect_price))
        assert current_price >= expect_price

    def teardown(self):
        App().quit()
