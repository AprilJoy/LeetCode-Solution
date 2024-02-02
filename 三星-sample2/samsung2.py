#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: shaoyangdong shaoyangdong@gmail.com
@ Date: 2023-11-06 10:25:41
@ LastEditors: dongshaoyang shaoyangdong@gmail.com
@ LastEditTime: 2024-02-02 18:55:32
@ FilePath: /LeetCode-Solution/三星-sample2/samsung2.py
@ Description: 
@ 
@ Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''

def test():
  '''
 @ description: 
    @ param {type} 
   @ return: 
   '''
  pass

import itertools
import os

class Location:
    def __init__(self,x,y):
        self.x = x
        self.y = y
def calculate_distance(point1, point2):
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)

def calculate_path_length(graph, path):
    # 计算给定path路径的总长度
    length = 0
    for i in range(len(path) - 1):
        length += graph[path[i]][path[i + 1]]
    return length

def tsp(graph, start, end):
    # 获取所有城市的列表，除了起点和终点
    cities = list(graph.keys())
    print(cities)
    cities.remove(start)
    cities.remove(end)

    # 生成所有可能的城市排列
    permutations = list(itertools.permutations(cities))

    # 初始化最短路径长度为正无穷
    shortest_distance = float('inf')
    # 初始化最短路径为空
    shortest_path = None

    # 遍历所有排列
    for perm in permutations:
        # 在排列前后添加起点和终点
        path = [start] + list(perm) + [end]
        # 计算路径长度
        distance = calculate_path_length(graph, path)

        # 更新最短路径和长度
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = path

    return shortest_path, shortest_distance

if __name__ == "__main__":
    in_path = open(os.path.dirname(__file__)+ "/input2.txt","r")
    content = in_path.read().splitlines()
    # 生成城市的坐标字典，其中起点和终点的坐标已给出
    city_coordinates = {}

    for i in range(0, len(content), 2):
        num, = map(int, content[i].split())
        li = list(map(int, content[i+1].split()))

    
        for i in range(0, len(li), 2):
            if i == 0:
                city_coordinates['start']=Location(li[i], li[i+1])
                continue
            if i == 2:
                city_coordinates['end']=Location(li[i], li[i+1])
                continue
            city_coordinates[str(i//2)]=Location(li[i], li[i+1])

        # 起点和终点
        start_city = 'start'
        end_city = 'end'

        # 根据城市坐标生成距离图  距离值
        city_graph = {city: {other_city: calculate_distance(city_coordinates[city], city_coordinates[other_city])
                        for other_city in city_coordinates if city != other_city}
                for city in city_coordinates}


        # 解决 TSP 问题
        result_path, result_distance = tsp(city_graph, start_city, end_city)
        # 输出结果
        print(f"Shortest Path from {start_city} to {end_city}: {result_path}")
        print(f"Shortest Distance: {result_distance}")
