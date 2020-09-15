# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 39数组中出现次数超过一半的数字.py
# @date: 2020/07/18
"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

摩尔投票法
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0
        for num in nums:
            if vote == 0:
                x = num
            vote += 1 if num == x else -1
        return x
