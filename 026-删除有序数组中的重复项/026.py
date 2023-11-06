#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: shaoyangdong shaoyangdong@gmail.com
@ Date: 2023-11-06 10:25:41
@ LastEditors: shaoyangdong shaoyangdong@gmail.com
@ LastEditTime: 2023-11-06 10:49:08
@ FilePath: /LeetCode-Solution/026-删除有序数组中的重复项/026.py
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
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i = i +1
                nums[i] = nums[j]
            j = j+1
        return i + 1

if __name__ == "__main__":
    test()
    sol = Solution()

    # 定义测试用例
    test_case_1 = [0,0,1,1,3,4]

    # 测试用例1
    result_1 = sol.removeDuplicates(test_case_1)
    print(f"Test Case 1: {test_case_1}")
    print(f"Test Case 1 result: {result_1}\n") 
