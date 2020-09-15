# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 38字符串的排列.py
# @date: 2020/07/21
"""
输入一个字符串，打印出该字符串中字符的所有排列。

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

树的深度优先搜索
"""
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        chars, res = list(s), []

        def dfs(x):
            if x == len(chars) - 1:  # 递归终止条件
                res.append("".join(chars))
                return
            dic = set()
            for i in range(x, len(chars)):
                if chars[i] in dic:  # 重复，剪枝
                    continue
                dic.add(chars[i])
                chars[i], chars[x] = chars[x], chars[i]  # 交换，将c[i]固定在第x位
                dfs(x + 1)
                chars[i], chars[x] = chars[x], chars[i]  # 还原

        dfs(0)
        return res
