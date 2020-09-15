# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 003矩阵中的路径.py
# @date: 2020/06/21
"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 例如
| a  b  c  e |
| s  f  c  s |
| a  d  e  e |
矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""


class Solution:
    def __init__(self):
        self.d: list = [-1, 0, 1, 0, -1]

    def __dfs(self, x: int, y: int, pos: int) -> bool:
        # 判断边界是否越界
        if x < 0 or y < 0 or x >= self.rows or y >= self.cols:
            return False

        ch = self.matrix[x * self.cols + y]
        # 判断是否访问过，是否和字符串path[pos]匹配
        if (
            self.matrix[x * self.cols + y] == "#"
            or self.matrix[x * self.cols + y] != self.path[pos]
        ):
            return False

        # 如果匹配，判断是否匹配到最后一个字符
        if pos == (len(self.path) - 1):
            return True
        # 标记一下，下次不能再次进入
        self.matrix[x * self.cols + y] = "#"

        for i in range(4):
            if self.__dfs(x + self.d[i], y + self.d[i + 1], pos + 1):
                return True

        # 如果4个方向都无法匹配 tr[pos + 1]，则回溯， 将'#'还原成ch
        self.matrix[x * self.cols + y] = ch
        return False

    def hasPath(self, matrix: str, rows: int, cols: int, path: str):
        self.matrix = [t for t in matrix]
        self.rows = rows
        self.cols = cols
        self.path = path

        # 对每个位置上的字母作起点进行DFS
        for i in range(rows):
            for j in range(cols):
                if self.__dfs(i, j, 0):
                    return True
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.hasPath("ABCESFCSADEE", 3, 4, "ABCCED"))
