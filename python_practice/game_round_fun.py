#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : game_round_fun.py
# @Author: xrhuang
# @Date  : 2020/10/24 11:01 上午
# @Desc  : 回合制游戏

"""
- 一个回合制游戏，每个角色都有hp和power，hp代表血量，power代表攻击力，hp点初始值为1000，power的初始值为200
- 定义一个fight方法
    - `my_final_hp = my_hp - enemy_power`
    - `enemy_final_hp = enemy_hp - my_power`
    - 两个hp进行对比，血量剩余多的人获胜
"""
# 导入random包
import random


# 定义fight函数实现游戏逻辑
def fight(enemy_hp, enemy_power):
    # 定义4个变量存放数据
    my_hp = 1000
    my_power = 200

    # 打印敌人的血量和攻击力
    print(f"敌人的血量为{enemy_hp}, 攻击力为{enemy_power}")

    # 加入循环，让游戏可以进行多轮
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        # 判断输赢
        if my_hp <= 0:
            # 打印我和敌人的剩余血量
            print(f"我的剩余血量为{my_hp}")
            print(f"敌人的剩余血量为{enemy_hp}")
            print("你输了")
            break
        elif enemy_hp <= 0:
            print(f"我的剩余血量为{my_hp}")
            print(f"敌人的剩余血量为{enemy_hp}")
            print("你赢了")
            break


if __name__ == '__main__':
    # 列表推导式生成hp
    hp_list = [x for x in range(990, 1010)]

    # 从hp中选取一个值作为敌人的血量
    enemy_hp = random.choice(hp_list)

    # 敌人的攻击力用randint方法生成随机整数
    enemy_power = random.randint(190, 210)

    # 调用函数，传入敌人的hp和power
    fight(enemy_hp, enemy_power)
