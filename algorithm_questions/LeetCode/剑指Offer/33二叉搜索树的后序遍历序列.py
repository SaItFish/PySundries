# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 33二叉搜索树的后序遍历序列.py
# @date: 2020/07/17
"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3

示例 1：
输入: [1,6,3,2,5]
输出: false

示例 2：
输入: [1,3,2,6,5]
输出: true

通过区间遍历，后序遍历的最后一个节点为根节点
"""


class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j:  # [i,j] 区间
                return True  # 当 i>=j ，说明此子树节点数量<=1 ，无需判别正确性，因此直接返回 true
            p = i
            while postorder[p] < postorder[j]:
                p += 1
            m = p
            while postorder[p] > postorder[j]:
                p += 1
            # 判断此树是否正确，左子树是否正确，右子树是否正确
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)
