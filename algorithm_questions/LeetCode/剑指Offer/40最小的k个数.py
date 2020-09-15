# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 40最小的k个数.py
# @date: 2020/07/18
"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]

限制：
0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000

布隆过滤器, 快速排序
"""
from typing import List


class Solution:
    def quick_sort(self, arr: List[int], k: int) -> List[int]:
        def partition(arr, first, last):
            pivot = arr[last]
            i = first
            for j in range(first, last):  # 不取 last
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1

            arr[i], arr[last] = arr[last], arr[i]

            return i  # 分割点

        l = len(arr)
        if (l == 0) or (k > l):
            return
        if k == 0:
            return []
        if k == l:  # 不加此可能会有 bug
            return arr
        if l == 1:
            return arr

        # 快速排序法
        left, right = 0, len(arr) - 1
        while left <= right:  # 这里其实也相当于是二分法
            split_ind = partition(arr, left, right)
            if split_ind == k:  # 在 split_ind 左边有 k 个元素，全部不大于 pivot
                break
            elif split_ind > k:
                right = split_ind - 1
            else:
                left = split_ind + 1

        return arr[:k]

    def bloom_filter(self, arr: List[int], k: int) -> List[int]:
        bloom = [0 for _ in range(10000)]
        for num in arr:
            bloom[num] += 1
        res, i = [], 0
        while len(res) < k:
            if bloom[i] >= 1:
                for _ in range(bloom[i]):
                    res.append(i)
            i += 1
        return res[:k]
