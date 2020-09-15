# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 095不同的二叉搜索树2.py
# @date: 2020/07/26
"""
给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。

示例：
输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""
from typing import List
import copy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n < 1:
            return []
        pre = [TreeNode(1)]
        for i in range(2, n + 1):
            cur = []
            # 遍历之前的所有解
            for root in pre:
                # 第一种情况：新节点作为根节点
                new_root = TreeNode(i)
                new_root.left = root
                cur.append(copy.deepcopy(new_root))
                # 第二种情况：新节点插入右孩子，原来的右孩子作为新节点的左孩子
                move = root
                while move.right:
                    node = TreeNode(i)
                    # 插入
                    move.right, node.left = node, move.right
                    cur.append(copy.deepcopy(root))
                    # 恢复
                    move.right = node.left
                    # 移动
                    move = move.right
                # 第三种情况：新节点为最右边的叶子节点
                move.right = TreeNode(i)
                cur.append(copy.deepcopy(root))
                move.right = None
            pre = cur.copy()
        return pre


class Solution2:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTrees(start, end):
            if start > end:
                return [
                    None,
                ]

            allTrees = []
            for i in range(start, end + 1):  # 枚举可行根节点
                # 获得所有可行的左子树集合
                leftTrees = generateTrees(start, i - 1)

                # 获得所有可行的右子树集合
                rightTrees = generateTrees(i + 1, end)

                # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)

            return allTrees

        return generateTrees(1, n) if n else []


if __name__ == "__main__":
    solu = Solution()
    solu.generateTrees(3)
