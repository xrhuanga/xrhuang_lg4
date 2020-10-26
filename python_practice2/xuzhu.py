#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : xuzhu.py
# @Author: xrhuang
# @Date  : 2020/10/27 12:41 上午
# @Desc  : 定义XuZhu类，继承于TongLao类
"""
- 定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
- 加入模块化改造
"""
# 导入TongLao类
from python_practice2.tonglao import TongLao


# 定义XuZhu类，继承于TongLao类
class XuZhu(TongLao):
    # 定义read实例方法，打印：罪过罪过
    def read(self):
        print("罪过罪过")


if __name__ == '__main__':
    xuzhu = XuZhu(100, 100)
    xuzhu.read()
