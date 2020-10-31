# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @file: main.py
# @date: 2020/10/29


class Solution:
    def isUnique(self, astr: str) -> bool:
        for c in astr:
            if astr.count(c) > 1:
                return False
        return True
