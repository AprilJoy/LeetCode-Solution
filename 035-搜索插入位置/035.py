#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: 董少洋 dongshaoyang@sinochem.com
@ Date: 2023-10-23 13:56:10
@ LastEditors: dongshaoyang shaoyangdong@gmail.com
@ LastEditTime: 2024-02-02 21:47:31
@ FilePath: /LeetCode-Solution/035-搜索插入位置/035.py
@ Description: 
@ 
@ Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''

from typing import List

def test():
  '''
 @ description: 
    @ param {type} 
   @ return: 
   '''
  pass

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, up = 0, len(nums) - 1
        mi = (lo+up) // 2
        while lo <= up:
            if nums[mi] == target: 
                return mi
            elif nums[mi] > target:
                up = mi - 1
            else:
                lo = mi + 1            
            mi = (lo + up) // 2
        return lo