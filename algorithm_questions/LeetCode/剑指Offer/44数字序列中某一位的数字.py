# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 44数字序列中某一位的数字.py
# @date: 2020/07/22
"""
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

示例 1：
输入：n = 3
输出：3

示例 2：
输入：n = 11
输出：0

"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        i, cur, nxt = 0, 0, 0
        while nxt < n:
            cur = (i + 1) * 9 * (10 ** i)
            nxt += cur
            i += 1
        n = n - (nxt - cur) - 1
        if i == 0:
            num = n
        else:
            num = 10 ** (i - 1) + n // i
        return int(str(num)[n % i])

    def findNthDigit_better(self, n: int) -> int:
        digit, start, count = 1, 1, 9
        while n > count:
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit
        return int(str(num)[(n - 1) % digit])


if __name__ == "__main__":
    solu = Solution()
    print(solu.findNthDigit(9))
