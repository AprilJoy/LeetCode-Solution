#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: shaoyang dongshaoyang@sinochem.com
@ Date: 2023-10-25 09:48:31
@ LastEditors: shaoyang dongshaoyang@sinochem.com
@ LastEditTime: 2023-10-25 09:48:49
@ FilePath: /LeetCode-Solution/003- 无重复字符的最长子串/003.py
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
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        dic = {}
        m = 0
        each=0
        while each  <len(s):
            if s[each] in dic :
                # max的作用是为了防止abba这种情况，左指针出现向左移动的情况，左指针在操作过程中只能往右移动！
                l = max(l,dic[s[each]]+1)
            dic[s[each]] = each
            m = max(m,each-l+1)
            each = each+1
        return m

if __name__ == "__main__":
    test()
    # 创建Solution的实例
    sol = Solution()

    # 定义测试用例
    test_case_1 = "acebbcea"

    # 测试用例1
    result_1 = sol.lengthOfLongestSubstring(test_case_1)
    print(f"Test Case 1: {test_case_1}")
    print(f"Maximum Subarray Sum: {result_1}\n")    