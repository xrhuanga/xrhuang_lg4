#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : game_round_1.py
# @Author: xrhuang
# @Date  : 2020/10/24 09:55 上午
# @Desc  : 回合制游戏之一拳超人

"""
- 一个回合制游戏，每个角色都有hp和power，hp代表血量，power代表攻击力，hp点初始值为1000，power的初始值为200
- 定义一个fight方法
    - `my_final_hp = my_hp - enemy_power`
    - `enemy_final_hp = enemy_hp - my_power`
    - 两个hp进行对比，血量剩余多的人获胜
"""


# 定义fight函数实现游戏逻辑
def fight():
    # 定义4个变量存放数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    # 定义最终血量计算方式
    my_final_hp = my_hp - enemy_power
    enemy_final_hp = enemy_hp - my_power

    # if-else判断：判断输赢
    # if my_final_hp > enemy_final_hp:
    #     print("你赢了")
    # elif enemy_final_hp > my_final_hp:
    #     print("你输了")
    # else:
    #     print("平局")

    # 三目运算：比if-else语句简洁一些，仅适用于简单的判断语句
    print("你赢了") if my_final_hp > enemy_final_hp else print("你输了")


# 调用函数
fight()
