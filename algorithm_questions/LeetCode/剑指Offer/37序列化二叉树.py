# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 37序列化二叉树.py
# @date: 2020/07/18
"""
请实现两个函数，分别用来序列化和反序列化二叉树。

示例:
你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5
序列化为 "[1,2,3,null,null,4,5]"

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        res, queue = [], []
        queue.append(root)
        while queue:
            node: TreeNode = queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)
                res.append(str(node.val))
            else:
                res.append("None")
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return
        data = data.split(",")
        root = TreeNode(int(data[0]))
        queue, i = [root], 1
        while queue:
            node = queue.pop(0)
            if data[i] != "None":
                node.left = TreeNode(int(data[i]))
                queue.append(node.left)
            i += 1
            if data[i] != "None":
                node.right = TreeNode(int(data[i]))
                queue.append(node.right)
            i += 1
        return root
