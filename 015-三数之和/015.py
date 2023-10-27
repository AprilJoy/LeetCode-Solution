#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: shaoyang dongshaoyang@sinochem.com
@ Date: 2023-10-27 10:55:03
@ LastEditors: shaoyang dongshaoyang@sinochem.com
@ LastEditTime: 2023-10-27 10:55:19
@ FilePath: /LeetCode-Solution/015-三数之和/015.py
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

'''
通过先将数组排序，
然后设置2个指针，从头和尾两个方向，扫描整个数组，找到正确答案
'''
class Solution(object):
   def threeSum(self, nums) :
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                j, k, target = i + 1, len(nums) - 1, 0 - nums[i]
                while j < k:
                    if nums[j] + nums[k] == target:
                        res.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j+1]:
                            j += 1
                        while j < k and nums[k] == nums[k-1]:
                            k -= 1
                        j += 1
                        k -= 1
                    elif nums[j] + nums[k] < target:
                        j += 1
                    else:
                        k -= 1
        return res

if __name__ == "__main__":
    test()
        # 创建Solution的实例
    sol = Solution()

    # 定义测试用例
    test_case_1 = [-1,0,1,2,-1,-4]

    # 测试用例1
    result_1 = sol.threeSum(test_case_1)
    print(f"Test Case 1: {test_case_1}")
    print(f"Test Case 1 result: {result_1}\n")    
