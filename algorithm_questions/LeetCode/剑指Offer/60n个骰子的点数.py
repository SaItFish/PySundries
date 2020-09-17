# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 60n个骰子的点数.py
# @date: 2020/07/24
"""
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]

动态规划
"""
from typing import List


class Solution:
    def twoSum(self, n: int) -> List[float]:
        dp = [[0 for _ in range(6 * n + 1)] for _ in range(n + 1)]
        for i in range(1, 7):
            dp[1][i] = 1

        # 有i个骰子
        for i in range(2, n + 1):
            # i个骰子之和的数值
            for j in range(i, i * 6 + 1):
                # 当前骰子的数值
                for k in range(1, 7):
                    if j >= k + 1:
                        dp[i][j] += dp[i - 1][j - k]
        total, res = pow(6, n), []
        for i in range(n, n * 6 + 1):
            res.append(dp[n][i] * 1.0 / total)
        return res

    def twoSum_better(self, n: int) -> List[float]:
        dp = [0 for _ in range(6 * n + 1)]  # 索引0不取，后面取到最大索引6*n
        for i in range(1, 7):  # 初始化do，第一轮的抛掷
            dp[i] = 1
        # 从第二轮抛掷开始算
        for i in range(2, n + 1):
            # 第二轮抛掷最小和为2，从大到小更新对应的抛掷次数
            for j in range(6 * n, i - 1, -1):
                dp[j] = 0  # 每次投掷要从0更新dp[j]大小，点数和出现的次数要重新计算
                # 每次抛掷的点数
                for k in range(1, 7):
                    # 上一轮的最小点数为i-1
                    if j - k < i - 1:
                        break
                    # 根据上一轮来更新当前轮数据
                    dp[j] += dp[j - k]
        total, res = pow(6, n), []
        for i in range(n, 6 * n + 1):
            res.append(dp[i] * 1.0 / total)
        return res
