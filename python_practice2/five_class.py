#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : five_class.py
# @Author: xrhuang
# @Date  : 2020/10/26 11:08 下午
# @Desc  : 用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。

"""
1.定义人类
属性：姓名、性别、年龄、身高、体重
方法：吃、喝、说话
"""


# 定义人类
class Human(object):
    # 构造函数接收外部变量，并用实例变量接收
    def __init__(self, name, gender, age, height, weight):
        self.name = name
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight

    # 定义说话的实例方法
    def speak(self):
        print(f"{self.name} is speaking!")

    # 定义吃的实例方法
    def eat(self):
        print(f"{self.name} is eating!")

    # 定义喝的实例方法
    def drink(self):
        print(f"{self.name} is drinking!")


"""
2.定义手机类
属性：品牌、型号、电量、系统、系统版本
方法：打电话、发短信、手机支付
"""


# 定义手机类
class Phone(object):
    # 构造函数接收外部变量，并用实例变量接收
    def __init__(self, brand, pattern, power, system, system_version):
        self.brand = brand
        self.pattern = pattern
        self.power = power
        self.system = system
        self.system_version = system_version

    # 定义打电话的实例方法
    def call(self):
        print(f"use {self.brand} to call someone!")

    # 定义发短信的实例方法
    def message(self):
        print(f"use {self.brand} to send a message!")

    # 定义支付的实例方法
    def pay(self):
        print(f"use {self.brand} to pay!")


"""
3.定义汽车类
属性：品牌、型号、油量、颜色、座位数
方法：开车、鸣喇叭、刹车
"""


# 定义车类
class Car(object):
    # 构造函数接收外部变量，并用实例变量接收
    def __init__(self, brand, pattern, volume, color, seat_number):
        self.brand = brand
        self.pattern = pattern
        self.volume = volume
        self.color = color
        self.seat_number = seat_number

    # 定义开车的实例方法
    def run(self):
        print(f"use {self.brand} is running!")

    # 定义鸣喇叭的实例方法
    def honk(self):
        print(f"use {self.brand} is honking!")

    # 定义刹车的实例方法
    def brake(self):
        print(f"use {self.brand} is braking!")


"""
4.定义教师类
属性：名字、性别、教学年限、教导课程、级别
方法：备课、上课、改试卷
"""


# 定义教师类
class Teacher(object):
    # 构造函数接收外部变量，并用实例变量接收
    def __init__(self, name, gender, teaching_age, subject, level):
        self.name = name
        self.gender = gender
        self.teaching_age = teaching_age
        self.subject = subject
        self.level = level

    # 定义教师备课的实例方法
    def prepare(self):
        print(f"{self.name} is preparing a class!")

    # 定义教师上课的实例方法
    def teach(self):
        print(f"use {self.name} is teaching a class!")

    # 定义教师批改试卷的实例方法
    def revise(self):
        print(f"use {self.name} is revising the examination papers!")


"""
5.定义菜鸟驿站类
属性：驿站地址、驿站开启时间、驿站关闭时间、驿站评分、驿站工作人员数
方法：接收快递、取出快递
"""


# 定义菜鸟驿站类
class CaiNiaoYiZhan(object):
    # 构造函数接收外部变量，并用实例变量接收
    def __init__(self, address, open_time, close_time, score, worker_number):
        self.address = address
        self.open_time = open_time
        self.close_time = close_time
        self.score = score
        self.worker_number = worker_number

    # 定义驿站接收快递的实例方法
    def receive_express(self):
        print(f"{self.address} is receiving express!")

    # 定义驿站取出快递的实例方法
    def take_express(self):
        print(f"{self.address} is taking express!")
