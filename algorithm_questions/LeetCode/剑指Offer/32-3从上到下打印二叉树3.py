# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 32-3从上到下打印二叉树3.py
# @date: 2020/07/21
"""
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

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
  [20,9],
  [15,7]
]

双端队列
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
        res, deque = [], collections.deque()
        deque.append(root)
        while deque:
            tmp = []
            # 打印奇数层
            for _ in range(len(deque)):
                # 从左向右打印
                node = deque.popleft()
                tmp.append(node.val)
                # 先左后右加入下层节点
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(tmp)
            if not deque:
                break  # 若为空则提前跳出
            # 打印偶数层
            tmp = []
            for _ in range(len(deque)):
                # 从右向左打印
                node = deque.pop()
                tmp.append(node.val)
                # 先右后左加入下层节点
                if node.right:
                    deque.appendleft(node.right)
                if node.left:
                    deque.appendleft(node.left)
            res.append(tmp)
        return res

    def levelOrder_better(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp[::-1] if len(res) % 2 else tmp)
        return res
