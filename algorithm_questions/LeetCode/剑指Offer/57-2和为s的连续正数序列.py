# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 57-2和为s的连续正数序列.py
# @date: 2020/07/23
"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

示例 1：
输入：target = 9
输出：[[2,3,4],[4,5]]

示例 2：
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]

滑动窗口
"""
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i, j = 1, 2
        res = []
        while i <= target // 2:
            cur = sum(range(i, j + 1))
            if cur == target:
                res.append(list(range(i, j + 1)))
                j += 1
            elif cur < target:
                j += 1
            elif cur > target:
                i += 1
        return res

    def findContinuousSequence_better(self, target: int) -> List[List[int]]:
        i, j, s = 1, 1, 0
        res = []

        while i <= target // 2:
            if s < target:
                # 右边界向右移动
                s += j
                j += 1
            elif s > target:
                # 左边界向右移动
                s -= i
                i += 1
            else:
                # 记录结果
                res.append(list(range(i, j)))
                # 左边界向右移动
                s -= i
                i += 1
        return res


if __name__ == "__main__":
    solu = Solution()
    print(solu.findContinuousSequence(9))
