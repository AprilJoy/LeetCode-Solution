#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: dongshaoyang shaoyangdong@gmail.com
@ Date: 2024-02-05 16:51:08
@ LastEditors: dongshaoyang shaoyangdong@gmail.com
@ LastEditTime: 2024-02-05 17:03:10
@ FilePath: /LeetCode-Solution/二叉树/dfs.py
@ Description: 
@ 
@ Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

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
    def pre_dfs(self, root: TreeNode):
        """前序遍历"""
        if root is None: return
        # 顺序：根节点 -> 左子树 -> 右子树
        res.append(root.val)
        self.pre_dfs(root.left)
        self.pre_dfs(root.right)
    
    def in_dfs(self, root:TreeNode):
        if root is None: return 
        self.in_dfs(root.left)
        res.append(root.val)
        self.in_dfs(root.right)

    def post_dfs(self, root:TreeNode):
        if root is None: return 
        self.post_dfs(root.left)
        
        self.post_dfs(root.right)
        res.append(root.val)



if __name__ == "__main__":
    test()
    res = []
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
    #result = solution.pre_dfs(root)
    # result = solution.in_dfs(root)
    result = solution.post_dfs(root)
    print(res)