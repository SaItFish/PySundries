# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 64求1+2+…+n.py
# @date: 2020/07/24
"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

示例 1：
输入: n = 3
输出: 6

示例 2：
输入: n = 9
输出: 45

"""


class Solution:
    def sumNums(self, n: int) -> int:
        def multi(a, b):
            res = 0
            while b:
                if b & 1:
                    res += a
                a <<= 1
                b >>= 1
            return res

        return multi(n, n + 1) >> 1
