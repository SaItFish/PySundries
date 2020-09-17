# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 32-2从上到下打印二叉树2.py
# @date: 2020/07/21
"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]

BFS
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
        return res

    def my_levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        # 在queue中间插入标记node
        res, temp, queue = [], [], collections.deque()
        queue.append(root)
        queue.append(TreeNode("#"))
        while queue:
            node = queue.popleft()
            if node.val == "#":
                if not temp:
                    break
                res.append(temp.copy())
                temp.clear()
                queue.append(TreeNode("#"))
                continue
            temp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
