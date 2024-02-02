#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: 董少洋 dongshaoyang@sinochem.com
@ Date: 2023-10-23 13:56:10
@ LastEditors: dongshaoyang shaoyangdong@gmail.com
@ LastEditTime: 2024-02-02 22:17:31
@ FilePath: /LeetCode-Solution/三星-sample1/053.py
@ Description: 
@ 
@ Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_common_ancestor_and_subtree_size(root, v1, v2):
    def find_ancestor_and_size(node):
        # 辅助函数，递归查找公共祖先及其子树大小
        if not node:
            return 0

        # 递归查找左右子树的节点数
        left_size = find_ancestor_and_size(node.left)
        right_size = find_ancestor_and_size(node.right)

        # 如果当前节点是目标节点之一，则返回当前子树的总节点数（包括目标节点）
        if node.val == v1 or node.val == v2:
            return left_size + right_size + 1

        return left_size + right_size + 1

    def find_common_ancestor(node):
        # 辅助函数，递归查找最近公共祖先
        if not node:
            return None

        if node.val == v1 or node.val == v2:
            return node

        left_ancestor = find_common_ancestor(node.left)
        right_ancestor = find_common_ancestor(node.right)

        if left_ancestor and right_ancestor:
            return node
        elif left_ancestor:
            return left_ancestor
        else:
            return right_ancestor

    common_ancestor = find_common_ancestor(root)
    subtree_size = find_ancestor_and_size(common_ancestor)

    return common_ancestor.val, subtree_size

def build_tree_from_edges(vertices, edges):
    # 从边列表中构建二叉树
    node_dict = {i: TreeNode(i) for i in range(1, vertices + 1)}

    for i in range(0, len(edges), 2):
        parent_val, child_val = edges[i], edges[i + 1]
        parent_node, child_node = node_dict[parent_val], node_dict[child_val]

        if not parent_node.left:
            parent_node.left = child_node
        elif not parent_node.right:
            parent_node.right = child_node

    return node_dict[1]  # 假设根节点总是在索引 1 处

import os
def main():
    input_path = "input1.txt"
    with open(os.path.dirname(__file__)+ "/input1.txt","r") as file:
        content = file.read().splitlines()

    for i, line in enumerate(content, start=1):
        if i % 2 == 1:
            vertices, edges, v1, v2 = map(int, line.split())
        else:
            edges_list = list(map(int, line.split()))
            root = build_tree_from_edges(vertices, edges_list)
            common_ancestor, subtree_size = find_common_ancestor_and_subtree_size(root, v1, v2)
            print(f"#{i // 2 + 1} {common_ancestor} {subtree_size}")

if __name__ == "__main__":
    main()
