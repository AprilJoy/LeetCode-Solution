#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: 董少洋 dongshaoyang@sinochem.com
@ Date: 2023-10-23 13:56:10
@ LastEditors: 董少洋 dongshaoyang@sinochem.com
@ LastEditTime: 2023-10-23 14:11:19
@ FilePath: /LeetCode-Solution/53-最大数组和/053.py
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

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0: return 0
        res = now = nums[0]
        for i in range(1,l):
            if now > 0:
                now = now + nums[i]
            else:
                now = nums[i]
            if now > res:
                res = now
        return res
        
if __name__ == "__main__":
    test()
    # 创建Solution的实例
    sol = Solution()

    # 定义测试用例
    test_case_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    # 测试用例1
    result_1 = sol.maxSubArray(test_case_1)
    print(f"Test Case 1: {test_case_1}")
    print(f"Maximum Subarray Sum: {result_1}\n")    