# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @file: main.py
# @date: 2020/10/29
from collections import defaultdict


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        def create_dict(s: str):
            res = defaultdict(int)
            for c in s:
                res[c] += 1
            return res

        d1 = create_dict(s1)
        d2 = create_dict(s2)

        return d1 == d2
