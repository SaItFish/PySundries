# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 34二叉树中和为某一值的路径.py
# @date: 2020/07/18
"""
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]

深度优先搜索，剪枝
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []

        def dfs(node: TreeNode, tar: int):
            if not node:
                return
            path.append(node.val)
            tar -= node.val
            if tar == 0 and not node.left and not node.right:
                res.append(list(path))
            dfs(node.left, tar)
            dfs(node.right, tar)
            path.pop()

        dfs(root, sum)
        return res
