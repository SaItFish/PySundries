# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 16数值的整数次方.py
# @date: 2020/07/17
"""
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25

快速幂法  二分法
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        res = 1

        if n < 0:
            x, n = 1 / x, -n

        while n:
            if n & 1:  # 判断n最后一位是否为1，python按位操作运算符会将int转为二进制数
                res *= x
            x *= x
            n >>= 1

        return res
