# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 45把数组排成最小的数.py
# @date: 2020/07/19
"""
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

示例 1:
输入: [10,2]
输出: "102"

示例 2:
输入: [3,30,34,5,9]
输出: "3033459"

排序判断规则：设 nums 任意两数字的字符串格式 x 和 y ，则
若拼接字符串 x + y > y + x，则 x > y
反之，若 x + y < y + x ，则 x < y
使用上述比较大小的方法进行快速排序
"""
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        strs = [str(num) for num in nums]
        # 快速排序
        def fast_sort(left, right):
            if left >= right:
                return
            i, j = left, right
            while i < j:
                # 找到右侧较“小”的字符串
                while strs[j] + strs[left] >= strs[left] + strs[j] and i < j:
                    j -= 1
                # 找到左侧较“大”的字符串
                while strs[i] + strs[left] <= strs[left] + strs[i] and i > j:
                    i += 1
                # 交换两个字符串
                strs[i], strs[j] = strs[j], strs[i]
            # 将key置换到中间
            strs[i], strs[left] = strs[left], strs[i]
            fast_sort(left, i - 1)
            fast_sort(i + 1, right)

        fast_sort(0, len(nums) - 1)
        return "".join(strs)

    def minNumberSecond(self, nums: List[int]) -> str:
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(sort_rule))
        return "".join(strs)

