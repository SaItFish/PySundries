# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: 35复杂链表的复制.py
# @date: 2020/07/21
"""
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

示例:
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

深拷贝 图的搜索 Hash表
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        def dfs(node: Node):
            if not node:
                return None
            if node in visited:
                return visited[node]
            copy_node = Node(node.val, None, None)  # 创建新结点
            visited[node] = copy_node
            copy_node.next = dfs(node.next)
            copy_node.random = dfs(node.random)
            return copy_node

        def bfs(head):
            if not head:
                return head
            clone = Node(head.val, None, None)  # 创建新结点
            queue = collections.deque()
            queue.append(head)
            visited[head] = clone
            while queue:
                tmp = queue.pop()
                if tmp.next and tmp.next not in visited:
                    visited[tmp.next] = Node(tmp.next.val, [], [])
                    queue.append(tmp.next)
                if tmp.random and tmp.random not in visited:
                    visited[tmp.random] = Node(tmp.random.val, [], [])
                    queue.append(tmp.random)
                visited[tmp].next = visited.get(tmp.next)
                visited[tmp].random = visited.get(tmp.random)
            return clone

        visited = {}
        return dfs(head)
