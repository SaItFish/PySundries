# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 13机器人的运动范围.py
# @date: 2020/07/20
"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
输入：m = 2, n = 3, k = 1
输出：3

示例 2：
输入：m = 3, n = 1, k = 0
输出：1

深度优先搜索  广度优先搜索
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def check(num: int) -> int:
            temp = [int(x) for x in str(num)]
            return sum(temp)

        def dfs(x: int, y: int):
            # 是否越界，是否已经走过
            if x < 0 or x >= m or y < 0 or y >= n or mark[x][y] == 1:
                return False

            # 题目限制
            if check(x) + check(y) > k:
                return False

            # 标记走过的位置
            mark[x][y] = 1
            self.res += 1

            for i in range(4):
                dfs(x + d[i], y + d[i + 1])

        d: list = [-1, 0, 1, 0, -1]
        self.res, mark = 0, [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        dfs(0, 0)
        return self.res

    def moving_count_dfs(self, m: int, n: int, k: int) -> int:
        def dfs(i, j, si, sj):
            if i >= m or j >= n or k < si + sj or (i, j) in visited:
                return 0
            visited.add((i, j))
            return (
                1
                + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj)
                + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)
            )

        visited = set()
        return dfs(0, 0, 0, 0)

    def moving_count_bfs(self, m: int, n: int, k: int) -> int:
        queue, visited, = [(0, 0, 0, 0)], set()
        while queue:
            i, j, si, sj = queue.pop(0)
            if i >= m or j >= n or k < si + sj or (i, j) in visited:
                continue
            visited.add((i, j))
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))
        return len(visited)
