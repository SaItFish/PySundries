# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 002机器人的运动范围.py
# @date: 2020/06/20
"""
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

深度优先搜索，广度优先搜索
"""


class Solution:
    def __init__(self):
        self.d: list = [-1, 0, 1, 0, -1]
        self.ret: int = 0

    def __check(self, num: int) -> int:
        """
        对数字按位求和

        Args:
            num (int): 操作数

        Returns:
            int: 和
        """
        temp = [int(x) for x in str(num)]
        return sum(temp)

    def __dfs(self, x: int, y: int):
        """
        深度优先搜索

        Args:
            x (int): 横坐标
            y (int): 纵坐标
        """
        if x < 0 or x >= self.rows or y < 0 or y >= self.cols or self.mark[x][y] == 1:
            return

        if (self.__check(x) + self.__check(y)) > self.threshold:
            return

        self.mark[x][y] = 1
        self.ret += 1

        for i in range(4):
            self.__dfs(x + self.d[i], y + self.d[i + 1])

    def __bfs(self, x: int, y: int):
        """
        广度优先搜索

        Args:
            x (int): 横坐标
            y (int): 纵坐标
        """
        queue = [(x, y)]
        while queue:
            current = queue.pop(0)
            x, y = current[0], current[1]
            for i in range(4):
                a = x + self.d[i]
                b = y + self.d[i + 1]
                if (
                    a < 0
                    or a >= self.rows
                    or b < 0
                    or b >= self.cols
                    or self.mark[a][b] == 1
                ):
                    continue
                else:
                    queue.append((a, b))
            self.mark[x][y] = 1
            self.ret += 1

    def movingCount(self, threshold: int, rows: int, cols: int):
        self.threshold = threshold
        self.rows = rows
        self.cols = cols
        if threshold <= 0:
            return 0
        self.mark = [[-1 for _ in range(cols + 1)] for _ in range(rows + 1)]
        # self.__dfs(0, 0)
        self.__bfs(0, 0)
        return self.ret


if __name__ == "__main__":
    solution = Solution()
    print(solution.movingCount(10, 1, 100))
