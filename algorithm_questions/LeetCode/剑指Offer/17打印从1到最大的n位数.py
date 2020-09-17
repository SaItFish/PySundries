# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 17打印从1到最大的n位数.py
# @date: 2020/07/17
"""
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
"""
from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return list(range(1, 10 ** n))


# 通用大数解法
class Solution2:
    def printNumbers(self, n: int) -> [int]:
        def dfs(x):
            if x == n:
                s = "".join(num[self.start:])
                if s != "0":
                    res.append(int(s))
                if n - self.start == self.nine:
                    self.start -= 1
                return
            for i in range(10):
                if i == 9:
                    self.nine += 1
                num[x] = str(i)
                dfs(x + 1)
            self.nine -= 1

        num, res = ["0"] * n, []
        self.nine = 0
        self.start = n - 1
        dfs(0)
        return res
