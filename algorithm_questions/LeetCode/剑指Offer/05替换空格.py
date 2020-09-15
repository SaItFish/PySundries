# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 05替换空格.py
# @date: 2020/06/28
"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
"""


class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")


if __name__ == "__main__":
    solution = Solution()
    print(solution.replaceSpace("We are happy."))
