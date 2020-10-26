#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : tonglao.py
# @Author: xrhuang
# @Date  : 2020/10/27 12:05 上午
# @Desc  : 定义TongLao类

"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。
TongLao类里面有2个方法
- see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，如果传入“丁春秋”，打印“叛徒！我杀了你”
- fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
"""


# 定义TongLao类
class TongLao(object):
    # 构造方法定义实例变量：血量和武力值
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    # 定义see_people实例方法，传入一个位置参数：人物名称
    def see_people(self, name: str):
        # 如果传入的名称是无崖子或者是无崖子的首字母，打印：师弟!!!!
        if name.upper() == "WYZ" or name == "无崖子":
            print("师弟!!!!")
        # 如果传入的名称是李秋水或者是李秋水的首字母，打印：师弟是我的!
        elif name.upper() == "LQS" or name == "李秋水":
            print("师弟是我的!")
        # 如果传入的名称是丁春秋或者是丁春秋的首字母，打印：叛徒!我杀了你!
        elif name.upper() == "DCQ" or name == "丁春秋":
            print("叛徒!我杀了你!")
        # 如果传入的名称不是上述的任意一个，打印：你是何方神圣！
        else:
            print("你是何方神圣！")

    # 定义fight_zms实例方法，传入2个位置参数：敌人的血量、敌人的武力值
    def fight_zms(self, enemy_hp, enemy_power):
        # 武力值提升10倍
        self.power *= 10
        # 血量缩减2倍
        self.hp /= 2
        # 经过一回合战斗后，TongLao剩余的血量
        self.hp -= enemy_power
        # 经过一回合战斗后，敌人剩余的血量
        enemy_hp -= self.power
        # 如果TongLao的血量比敌人的血量多，打印：胜利了!
        if self.hp > enemy_hp:
            print("胜利了!")
        # 如果敌人的血量比TongLao的血量多，打印：输了!
        elif enemy_hp > self.hp:
            print("输了!")
        # 如果不是上述任意一种情况，打印：不分上下!
        else:
            print("不分上下!")


if __name__ == '__main__':
    tonglao = TongLao(100, 20)
    tonglao.see_people("WYZ")
    tonglao.see_people("李秋水")
    tonglao.see_people("dcq")
    tonglao.fight_zms(50, 20)
