# -*- coding: utf-8 -*-
# @Time:2024/5/28 21:12
# @Author：huanglijing

import pytest
import yaml


class TestData:
    @pytest.mark.parametrize(["a", "b"], yaml.safe_load(open("./data.yaml")))
    def test_data1(self, a, b):
        c = a + b
        print(c)
