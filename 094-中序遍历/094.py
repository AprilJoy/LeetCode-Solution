#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: shaoyangdong shaoyangdong@gmail.com
@ Date: 2023-10-30 15:45:29
@ LastEditors: dongshaoyang shaoyangdong@gmail.com
@ LastEditTime: 2024-02-05 17:35:26
@ FilePath: /LeetCode-Solution/094-中序遍历/094.py
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

class TreeNode:
   def __init__(self,val=0,left=None,right=None):
      self.val = val
      self.left = left
      self.right = right
      
class Solution:
   # 递归
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.inorder(root, res)
        return res
   
    def inorder(self, root:TreeNode, res: List[int]):
        if not root : return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right,res)

   # 迭代
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
        

      


       
if __name__ == "__main__":
    test()
        # 创建Solution的实例
    sol = Solution()

    # 定义测试用例
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)


    # result_2 = sol.inorderTraversal(root)

    result_2 = sol.inorderTraversal2(root)
    print(result_2)
