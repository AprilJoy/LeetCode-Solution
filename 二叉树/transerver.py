#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: dongshaoyang shaoyangdong@gmail.com
@ Date: 2024-02-04 17:43:39
@ LastEditors: dongshaoyang shaoyangdong@gmail.com
@ LastEditTime: 2024-02-05 16:49:44
@ FilePath: /LeetCode-Solution/二叉树/transerver.py
@ Description: 
@ 
@ Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

from typing import List, Optional
# 本质上就是BFS 广度优先遍历

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
    def levelOrder(self,root:Optional[TreeNode])->List[List[int]]:
        if root is None:
            return []
        ans = []
        cur = [root]
        while cur:
            nxt = []
            vals = []
            for node in cur:
                vals.append(node.val)
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            cur = nxt
            ans.append(vals)
        return ans

if __name__ == "__main__":
    test()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(6)

    # Creating an instance of the Solution class
    solution = Solution()

    # Testing the levelOrder method
    result = solution.levelOrder(root)

    # Expected output: [[1], [2, 3], [4, 5]]
    print(result)
