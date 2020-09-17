# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 53-1在排序数组中查找数字1.py
# @date: 2020/07/23
"""
统计一个数字在排序数组中出现的次数。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

二分法
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or nums[0] > target or nums[-1] < target:
            return 0
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] < target:
                i += 1
            if nums[j] > target:
                j -= 1
            if nums[i] == target and nums[j] == target:
                break
        else:
            if nums[i] == target:
                return 1
            return 0
        return j - i + 1

    def search_better(self, nums: [int], target: int) -> int:
        def helper(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] <= tar:
                    i = m + 1
                else:
                    j = m - 1
            return i

        return helper(target) - helper(target - 1)


if __name__ == "__main__":
    solu = Solution()
    solu.search([1], 1)
