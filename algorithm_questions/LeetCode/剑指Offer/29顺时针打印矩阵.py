# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 29顺时针打印矩阵.py
# @date: 2020/07/17
"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

边界问题
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        # 四个边界范围
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(l, r + 1):
                res.append(matrix[t][i])  # left to right
            t += 1
            if t > b:
                break
            for i in range(t, b + 1):
                res.append(matrix[i][r])  # top to bottom
            r -= 1
            if l > r:
                break
            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])  # right to left
            b -= 1
            if t > b:
                break
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])  # bottom to top
            l += 1
            if l > r:
                break
        return res
