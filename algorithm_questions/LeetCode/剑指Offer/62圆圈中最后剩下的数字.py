# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 62圆圈中最后剩下的数字.py
# @date: 2020/07/24
"""
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

示例 1：
输入: n = 5, m = 3
输出: 3
示例 2：
输入: n = 10, m = 17
输出: 2

"""


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        res = [x for x in range(n)]
        i = 0
        while len(res) > 1:
            i = (i + m - 1) % len(res)
            res.pop(i)
        return res[0]

    def lastRemaining_better(self, n: int, m: int) -> int:
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i
        return f


if __name__ == "__main__":
    solu = Solution()
    print(solu.lastRemaining(10, 17))
