# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 26树的子结构.py
# @date: 2020/07/17
"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：
输入：A = [1,2,3], B = [3,1]
输出：false

示例 2：
输入：A = [3,4,5,1,2], B = [4,1]
输出：true

先序遍历 递归
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B:  # B为空，匹配成功
                return True
            if not A or A.val != B.val:  # 树A为空或者两者值不相等，则匹配失败
                return False
            return recur(A.left, B.left) and recur(A.right, B.right)  # 否则匹配未完成

        return bool(A and B) and (  # 判断两棵树是否都为空
            recur(A, B)  # 匹配两棵树
            or self.isSubStructure(A.left, B)
            or self.isSubStructure(A.right, B)
        )
