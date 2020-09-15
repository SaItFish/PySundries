# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 005数据流中的中位数.py
# @date: 2020/06/22
"""
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。

插入排序  堆排序
"""


class Solution1:
    def __init__(self):
        self.nums = []

    def insert(self, num):
        if self.nums == []:
            self.nums.append(num)
        else:
            for i, x in enumerate(self.nums):
                if x > num:
                    self.nums.insert(i, num)
                    return
            self.nums.append(num)

    def get_median(self):
        i = len(self.nums)
        if i % 2 == 0:
            return (self.nums[i // 2] + self.nums[i // 2 - 1]) / 2.0
        else:
            return self.nums[i // 2]


if __name__ == "__main__":
    solution = Solution1()
    arr = [5, 2, 3, 4, 1, 6, 7, 0, 8]
    for num in arr:
        solution.insert(num)
        print(solution.nums)
