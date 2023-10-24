#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: shaoyang dongshaoyang@sinochem.com
@ Date: 2023-10-24 09:35:01
@ LastEditors: shaoyang dongshaoyang@sinochem.com
@ LastEditTime: 2023-10-24 09:41:15
@ FilePath: /LeetCode-Solution/001-两数之和/001.py
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

class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        numMap = {}
        r = []
        for i in range(len(nums)):
            if numMap.__contains__(target-nums[i]):
                r.append((numMap.get(target-nums[i]), i))
            else:
                numMap[nums[i]] = i
        return r
if __name__ == "__main__":
    test()
    # 创建Solution的实例
    sol = Solution()

    # 定义测试用例
    nums_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    target_1 = 3

    # 测试用例1
    result_1 = sol.twoSum(nums_1, target_1)
    print(f"Test Case 1: {nums_1}, {target_1}")
    print(f"Maximum Subarray Sum: {result_1}\n")    