# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 56-1数组中数字出现的次数1.py
# @date: 2020/07/23
"""
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

示例 1：
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]

示例 2：
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]

数位运算  异或
"""
from typing import List
import functools


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # 找到两个只出现一次的数字的异或值
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1
        while div & ret == 0:
            div <<= 1
        # 找到异或值中为1的位（在这个位上两个只出现一次的数字不同）
        a, b = 0, 0
        for n in nums:
            # 根据这个位对数组分类，求两块数组的异或值
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]
