# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 55-1二叉树的深度.py
# @date: 2020/07/23
"""
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node: TreeNode, depth: int):
            if not node:
                return
            self.res = max(depth, self.res)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 1)
        return self.res
