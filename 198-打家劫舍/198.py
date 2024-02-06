#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: shaoyangdong shaoyangdong@gmail.com
@ Date: 2023-10-30 15:45:29
@ LastEditors: dongshaoyang shaoyangdong@gmail.com
@ LastEditTime: 2024-02-05 23:27:41
@ FilePath: /LeetCode-Solution/198-打家劫舍/198.py
@ Description: 
@ 
@ Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''

from typing import List, Optional


def test():
  '''
 @ description: 
    @ param {type} 
   @ return: 
   '''
  pass

class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return nums[0]
        rob = [0] * l
        rob[0] = nums[0]
        rob[1] = max(nums[0], nums[1])

        for i in range(2, l):
            rob[i] = max(nums[i] + rob[i-2] , rob[i-1])
        return rob[-1]
        

      


       
if __name__ == "__main__":
    test()
        # 创建Solution的实例
    sol = Solution()

    # 定义测试用例
    input = [1,2,3,1]

    result_2 = sol.rob(input)
    print(result_2)
