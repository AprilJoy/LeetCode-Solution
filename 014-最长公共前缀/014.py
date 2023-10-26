#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: shaoyang dongshaoyang@sinochem.com
@ Date: 2023-10-26 10:04:28
@ LastEditors: shaoyang dongshaoyang@sinochem.com
@ LastEditTime: 2023-10-26 10:44:38
@ FilePath: /LeetCode-Solution/014-最长公共前缀/014.py
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
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: s
        """

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        # s1 = min(strs)
        # s2 = max(strs)

        # for index,ch in enumerate(s1):
        #     if ch !=s2[index]:
        #         return s1[:index]
        # return s1 
        if len(strs) == 1:
            return strs[0]
        pre = strs[0]
        pre_l = len(pre)
        for i in strs:


            while i[:pre_l] != pre[:pre_l] and pre_l>0:
                pre_l = pre_l - 1
        return pre[:pre_l]
    
    def longestCommonPrefix_1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        s1 = min(strs)
        s2 = max(strs)

        for index,ch in enumerate(s1):
            if ch !=s2[index]:
                return s1[:index]
        return s1 

if __name__ == "__main__":
    test()
        # 创建Solution的实例
    sol = Solution()

    # 定义测试用例
    test_case_1 = ["flower","flow","flight"]

    # 测试用例1
    result_1 = sol.longestCommonPrefix(test_case_1)
    print(f"Test Case 1: {test_case_1}")
    print(f"Maximum Subarray Sum: {result_1}\n")    


    result_1 = sol.longestCommonPrefix_1(test_case_1)
    print(f"Test Case 1: {test_case_1}")
    print(f"Maximum Subarray Sum: {result_1}\n")    