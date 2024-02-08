#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: shaoyangdong shaoyangdong@gmail.com
@ Date: 2023-10-30 15:45:29
@ LastEditors: dongshaoyang shaoyangdong@gmail.com
@ LastEditTime: 2024-02-06 17:18:41
@ FilePath: /LeetCode-Solution/062-不同路径/198.py
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
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]
        

      


       
if __name__ == "__main__":
    test()
        # 创建Solution的实例
    sol = Solution()

    # 定义测试用例
    m = 7
    n = 3

    result_2 = sol.uniquePaths(m,n)
    print(result_2)
