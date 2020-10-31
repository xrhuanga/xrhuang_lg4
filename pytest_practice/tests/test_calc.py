#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_calc.py
# @Author: xrhuang
# @Date  : 2020/10/31 10:49 上午
# @Desc  : 计算器功能测试用例
import allure
import pytest
from pytest_practice.core.calc import Calc


@allure.feature("计算器乘除法测试用例")
class TestCalc(object):

    def setup_class(self):
        self.calc = Calc()
        self.div = Calc()

    @allure.story("0与其他数值相乘")
    @pytest.mark.parametrize('a,b,expect', [
        [0, 0, 0],
        [0, 10, 0],
        [0, -100000, 0],
        [0, 0.1, 0],
        [0, 1e100, 0],
        [0, 1e-100, 0],
        [0, 1/3, 0]
    ])
    def test_mul_zero(self, a, b, expect):
        assert self.calc.mul(a, b) == expect

    @allure.story("正整数与其他数值相乘")
    @pytest.mark.parametrize('a,b,expect', [
        [1, 0, 0],
        [10, 2, 20],
        [2, -9, -18],
        [3, 0.3, 0.9],
        [4, -0.3, -1.2],
        [500000, 1e-20, 5e-15],
        [6000000, -1e-20, -6e-14],
        [70000000, 1/10, 7000000.0],
        [800000000, -1/10, -80000000.0]
    ])
    def test_mul_positive_int(self, a, b, expect):
        assert self.calc.mul(a, b) == expect

    @allure.story("负整数与其他数值相乘")
    @pytest.mark.parametrize('a,b,expect', [
        [-1, 0, 0],
        [-10, 2, -20],
        [-2, -9, 18],
        [-3, 0.3, -0.9],
        [-4, -0.3, 1.2],
        [-500000, 1e-20, -5e-15],
        [-6000000, -1e-20, 6e-14],
        [-70000000, 1 / 10, -7000000.0],
        [-800000000, -1 / 10, 80000000.0]
    ])
    def test_mul_negative_int(self, a, b, expect):
        assert self.calc.mul(a, b) == expect

    @allure.story("正小数与其他数值相乘")
    @pytest.mark.parametrize('a,b,expect', [
        [0.1, 0, 0],
        [10.2, 2, 20.2],
        [200.3, -2, -400.6],
        [3000.4, 0.3, 900.12],
        [40000.5, -0.3, -12000.15],
        [500000.6, 1e-20, 5.0006e-15],
        [6000000.8, -1e-20, -6.0000008e-14],
        [70000000.9, 1/10, 7000000.09],
        [800000000.10, -1/10, -80000000.01]
    ])
    def test_mul_positive_float(self, a, b, expect):
        assert self.calc.mul(a, b) == expect

    @allure.story("负小数与其他数值相乘")
    @pytest.mark.parametrize('a,b,expect', [
        [-0.1, 0, 0],
        [-10.2, 2, -20.2],
        [-200.3, -2, 400.6],
        [-3000.4, 0.3, -900.12],
        [-40000.5, -0.3, 12000.15],
        [-500000.6, 1e-20, -5.0006e-15],
        [-6000000.8, -1e-20, 6.0000008e-14],
        [-70000000.9, 1 / 10, -7000000.09],
        [-800000000.10, -1 / 10, 80000000.01]
    ])
    def test_mul_negative_float(self, a, b, expect):
        assert self.calc.mul(a, b) == expect

    @allure.story("异常相乘")
    @pytest.mark.parametrize('a,b', [
        [0, 'a'],
        ['b', 0],
        [1, 'c'],
        ['d', 2],
        [-3, 'e'],
        ['f', -4],
        [5.5, 'g'],
        ['f', 6.6],
        [-7.7, 'g'],
        ['h', -8.8],
        ['iii', 'jjj'],
        [True, False]
    ])
    def test_mul_error(self, a, b):
        with pytest.raises(BaseException):
            assert self.calc.mul(a, b)

    @allure.story("0与其他数值相除")
    @pytest.mark.parametrize('a,b,expect', [
        [0, 10, 0],
        [0, -100000, 0],
        [0, 0.1, 0.0],
        [0, 1e100, 0.0],
        [0, 1e-100, 0.0],
        [0, 1/3, 0.0]
    ])
    def test_div_zero(self, a, b, expect):
        assert self.calc.div(a, b) == expect

    @allure.story("正整数与其他数值相除")
    @pytest.mark.parametrize('a,b,expect', [
        [10, 2, 5],
        [2, -9, -0.2222222222222222],
        [3, 0.3, 10.0],
        [4, -0.3, -13.333333333333334],
        [500000, 1e-20, 5e+25],
        [6000000, -1e-20, -6e+26],
        [70000000, 1 / 10, 70000000.0],
        [800000000, -1 / 10, -800000000.0]
    ])
    def test_div_positive_int(self, a, b, expect):
        assert self.calc.mul(a, b) == expect

    @allure.story("负整数与其他数值相除")
    @pytest.mark.parametrize('a,b,expect', [
        [-10, 2, -5],
        [-2, -9, 0.2222222222222222],
        [-3, 0.3, -10.0],
        [-4, -0.3, 13.333333333333334],
        [-500000, 1e-20, -5e+25],
        [-6000000, -1e-20, 6e+26],
        [-70000000, 1 / 10, -70000000.0],
        [-800000000, -1 / 10, 800000000.0]
    ])
    def test_div_negative_int(self, a, b, expect):
        assert self.calc.mul(a, b) == expect

    @allure.story("正小数与其他数值相除")
    @pytest.mark.parametrize('a,b,expect', [
        [10.2, 2, 5.1],
        [200.3, -2, -100.15],
        [3000.4, 0.3, 10001.333333333334],
        [40000.5, -0.3, -133335.0],
        [500000.6, 1e-20, 5.000006e+25],
        [6000000.8, -1e-20, -6.0000008e+26],
        [70000000.9, 1/10, 700000009.0],
        [800000000.10, -1/10, -8000000001.0]
    ])
    def test_div_positive_float(self, a, b, expect):
        assert self.calc.mul(a, b) == expect

    @allure.story("负小数与其他数值相除")
    @pytest.mark.parametrize('a,b,expect', [
        [-10.2, 2, -5.1],
        [-200.3, -2, 100.15],
        [-3000.4, 0.3, -10001.333333333334],
        [-40000.5, -0.3, 133335.0],
        [-500000.6, 1e-20, -5.000006e+25],
        [-6000000.8, -1e-20, 6.0000008e+26],
        [-70000000.9, 1 / 10, -700000009.0],
        [-800000000.10, -1 / 10, 8000000001.0]
    ])
    def test_div_negative_float(self, a, b, expect):
        assert self.calc.mul(a, b) == expect

    @allure.story("异常相除")
    @pytest.mark.parametrize('a,b', [
        [0, 0],
        [1, 0],
        [2.0, 0],
        [-3.5, 0],
        [0, 'a'],
        ['b', 0],
        [1, 'c'],
        ['d', 2],
        [-3, 'e'],
        ['f', -4],
        [5.5, 'g'],
        ['f', 6.6],
        [-7.7, 'g'],
        ['h', -8.8],
        ['iii', 'jjj'],
        [True, False]
    ])
    def test_div_error(self, a, b):
        with pytest.raises(BaseException):
            assert self.calc.mul(a, b)
