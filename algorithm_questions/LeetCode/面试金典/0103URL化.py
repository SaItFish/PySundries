# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @file: main.py
# @date: 2020/10/29


class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        return S[:length].replace(" ", "%20")
