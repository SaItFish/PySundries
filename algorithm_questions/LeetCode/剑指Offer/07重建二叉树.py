# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 07重建二叉树.py
# @date: 2020/06/28
"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]

返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

前序遍历的第一个值为根节点的值，使用这个值将中序遍历结果分成两部分，左部分为树的左子树中序遍历结果，右部分为树的右子树中序遍历的结果。然后分别对左右子树递归地求解。
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recur(self, pre_root, in_left, in_right):
        if in_left > in_right:
            return  # 终止条件：中序遍历为空
        root = TreeNode(self.po[pre_root])  # 建立当前子树的根节点
        i = self.dic[self.po[pre_root]]  # 搜索根节点在中序遍历中的索引，从而可对根节点、左子树、右子树完成划分。
        root.left = self.recur(pre_root + 1, in_left, i - 1)  # 开启左子树的下层递归
        root.right = self.recur(
            i - in_left + pre_root + 1, i + 1, in_right
        )  # 开启右子树的下层递归
        return root  # 返回根节点，作为上层递归的左（右）子节点

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.dic, self.po = {}, preorder
        for i, x in enumerate(inorder):
            self.dic[x] = i
        return self.recur(0, 0, len(inorder) - 1)
