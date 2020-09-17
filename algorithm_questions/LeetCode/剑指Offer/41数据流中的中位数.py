# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 41数据流中的中位数.py
# @date: 2020/07/18
"""
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。

示例 1：
输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]

示例 2：
输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]

插入排序  小顶堆，大顶堆
"""
from heapq import *  # heapq 模块是小顶堆，大顶堆可以用负值存储
from typing import List


class MedianFinder:
    def __init__(self):
        self.A = []  # 小顶堆，保存较大的一半
        self.B = []  # 大顶堆，保存较小的一半

    def addNum(self, num: int) -> None:
        # heappushpop插入num，从堆顶弹出一个值
        if len(self.A) != len(self.B):
            # 将新元素 num 插入至 A ，再将 A 堆顶元素插入至 B
            heappush(self.B, -heappushpop(self.A, num))
        else:
            # 将新元素 num 插入至 B ，再将 B 堆顶元素插入至 A
            heappush(self.A, -heappushpop(self.B, -num))

    def findMedian(self) -> float:
        return (
            self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0
        )


class MedianFinderInsert:
    def __init__(self):
        self.nums: List[int] = []

    def addNum(self, num: int) -> None:
        if self.nums == []:
            self.nums.append(num)
        else:
            for i, x in enumerate(self.nums):
                if x >= num:
                    self.nums.insert(i, num)
                    return
            self.nums.append(num)

    def findMedian(self) -> float:
        length = len(self.nums)
        return (
            (self.nums[length // 2] + self.nums[length // 2 - 1]) / 2.0
            if length % 2 == 0
            else self.nums[length // 2]
        )
