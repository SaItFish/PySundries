# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 101对称二叉树.py
# @date: 2020/07/29
"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def traversal(L: TreeNode, R: TreeNode):
            if not L and not R:
                return True
            if not L or not R or L.val != R.val:
                return False
            return traversal(L.left, R.right) and traversal(L.right, R.left)

        return traversal(root.left, root.right) if root else True
