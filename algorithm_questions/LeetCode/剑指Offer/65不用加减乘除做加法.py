# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 65不用加减乘除做加法.py
# @date: 2020/07/24
"""
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

示例:

输入: a = 1, b = 1
输出: 2

提示：
a, b 均可能是负数或 0
结果不会溢出 32 位整数

"""


class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xFFFFFFFF
        # python是以补码存储数字
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7FFFFFFF else ~(a ^ x)
