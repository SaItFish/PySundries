# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 001剪绳子.py
# @date: 2020/06/20
"""
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[1],...,k[m]。请问k[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
输入描述:
    输入一个数n，意义见题面。（2 <= n <= 60）
输出描述:
    输出答案。
示例1
    输入 8
    输出 18

本题目使用动态规划
"""


def cutRope(number: int):
    """
    剪绳子

    Args:
        number (int): 绳子长度

    Returns:
        [int]: 最大乘积
    """
    temp = [-1 for _ in range(number + 1)]
    # 对长度为2和3的值特殊处理
    if number == 2:
        return 1
    elif number == 3:
        return 2

    # 初始化前四个数
    for i in range(1, 5):
        temp[i] = i

    # 保存最优解
    for i in range(5, number + 1):
        for j in range(1, i):
            temp[i] = max(temp[i], j * temp[i - j])

    return temp[number]


if __name__ == "__main__":
    print(cutRope(4))
