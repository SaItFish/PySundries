# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 111二叉树的最小深度.py
# @date: 2020/07/30
"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

BFS 剪枝
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        else:
            node_deque = deque([(1, root), ])

        while node_deque:
            depth, root = node_deque.popleft()
            children = [root.left, root.right]
            # any: Return True if bool(x) is True for any x in the iterable. If the iterable is empty, return False.
            if not any(children):
                return depth
            for c in children:
                if c:
                    node_deque.append((depth + 1, c))
