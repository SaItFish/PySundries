# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 006二叉搜索树的第k个节点.py
# @date: 2020/06/23
"""
给定一棵二叉搜索树，请找出其中的第k小的结点。例如，(5，3，7，2，4，6，8) 中，按结点数值大小顺序第三小结点的值为4。

猜测：DFS
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):

        pass
