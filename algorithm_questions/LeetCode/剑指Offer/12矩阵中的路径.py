# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 12矩阵中的路径.py
# @date: 2020/07/14
"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
 ["s","f","c","s"],
 ["a","d","e","e"]]

但矩阵中不包含字符串"abfb"的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

DFS
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.d = [-1, 0, 1, 0, -1]
        self.board = board
        self.word = word
        self.rows = len(board)
        self.cols = len(board[0])
        # 对每一个位置上的字母作为起点循环
        for i in range(self.rows):
            for j in range(self.cols):
                if self.__dfs(i, j, 0):
                    return True
        return False

    def __dfs(self, x: int, y: int, pos: int):
        # 判断边界
        if x < 0 or x >= self.rows or y < 0 or y >= self.cols:
            return False

        # 将字母保存下来
        ch = self.board[x][y]
        if ch == "#" or ch != self.word[pos]:
            return False

        if pos == len(self.word) - 1:
            return True

        self.board[x][y] = "#"

        for i in range(4):
            if self.__dfs(x + self.d[i], y + self.d[i + 1], pos + 1):
                return True

        self.board[x][y] = ch
        return False

