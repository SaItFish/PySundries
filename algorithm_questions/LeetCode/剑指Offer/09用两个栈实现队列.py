# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 09用两个栈实现队列.py
# @date: 2020/06/28
"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：
输入：
    执行的方法：["CQueue","appendTail","deleteHead","deleteHead"]
    使用的参数：[[],[3],[],[]]
输出：[null,null,3,-1]

示例 2：
输入：
    执行的方法：["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
    使用的参数：[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]

"""


class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B:  # 当B中仍有已经倒序的元素，B顶端仍为最先放入的元素，弹出B顶端元素
            return self.B.pop()
        if not self.A:  # A, B都没有元素，返回-1
            return -1
        while self.A:  # 将A内的元素倒入B中
            self.B.append(self.A.pop())
        return self.B.pop()
