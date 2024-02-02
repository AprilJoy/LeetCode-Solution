#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: dongshaoyang shaoyangdong@gmail.com
@ Date: 2024-02-02 20:07:53
@ LastEditors: dongshaoyang shaoyangdong@gmail.com
@ LastEditTime: 2024-02-02 21:15:34
@ FilePath: /LeetCode-Solution/三星-sample3/samsung3.py
@ Description: 
@ 
@ Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

def test():
  '''
 @ description: 
    @ param {type} 
   @ return: 
   '''
  pass

import os
def find_task_order(graph):
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        order.append(node)

    V = len(graph) - 1  # 总顶点数
    visited = [False] * (V + 1)
    order = []

    for node in range(1, V + 1):
        if not visited[node]:
            dfs(node)

    # 结果以逆序输出
    result = reversed(order)
    return result


def main():

    
    in_path = open(os.path.dirname(__file__)+ "/input3.txt","r")
    content = in_path.read().splitlines()

    for i in range(0, len(content), 2):
        vertex, edges_num = map(int, content[i].split())
        edges = list(map(int, content[i+1].split()))
        # 1.构建图
        graph = {i: [] for i in range(vertex + 1)}
        
        for j in range(0, len(edges), 2):
            graph[edges[j]].append(edges[j+1])
        # 2.查找任务顺序
        task_order = find_task_order(graph)
        # 3.输出结果
        print(f"#{i//2 + 1} {' '.join(map(str, task_order))}")

if __name__ == "__main__":
    main()
