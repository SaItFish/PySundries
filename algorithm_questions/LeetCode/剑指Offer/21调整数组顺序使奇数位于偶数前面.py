# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 21调整数组顺序使奇数位于偶数前面.py
# @date: 2020/07/17
"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。

双指针
"""
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if num & 1:  # 奇数
                res.insert(0, num)
            else:
                res.append(num)
        return res

    def better(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1:  # 当为奇数时跳过
                i += 1
            while i < j and nums[j] & 1 == 0:  # 当为偶数时跳过
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]  # 互换两指针的值
        return nums
