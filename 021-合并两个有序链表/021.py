#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: shaoyangdong shaoyangdong@gmail.com
@ Date: 2023-10-30 15:45:29
@ LastEditors: shaoyangdong shaoyangdong@gmail.com
@ LastEditTime: 2023-10-31 09:35:50
@ FilePath: /LeetCode-Solution/021-合并两个有序链表/021.py
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

class ListNode:
   def __init__(self, x) -> None:
      self.value = x
      self.next = None

def create_list_node(values):
    if not values:
        return None

    # 创建链表头节点
    head = ListNode(values[0])
    current = head

    # 依次创建并连接节点
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dum = ListNode(None)
        prev = dum

        while l1 and l2:
            if l1.value < l2.value:
              prev.next = l1
              l1 = l1.next
            else:
              prev.next = l2
              l2 = l2.next
            prev = prev.next
            
        if l1 == None:
           prev.next = l2
        if l2 == None:
           prev.next = l1
        return dum.next

    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
       if l1 == None:
          return l2
       if l2 == None:
          return l1
       if l1.value < l2.value:
          l1.next = self.mergeTwoLists1(l1.next, l2)
          return l1
       else:
          l2.next = self.mergeTwoLists1(l1, l2.next)
          return l2
  
       
if __name__ == "__main__":
    test()
        # 创建Solution的实例
    sol = Solution()

    # 定义测试用例
    test_case_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    l1 = [1,2,4]
    l2 = [1,3,4]
    l1_head = create_list_node(l1)
    l2_head = create_list_node(l2)
    # 打印链表
    # current = l1_head
    # while current:
    #     print(current.value)
    #     current = current.next

    # 测试用例1 两种方法不能同时用，l1_head的地址在使用过一次之后，会变成独立指针，指向自己
    # result_1 = sol.mergeTwoLists(l1_head, l2_head)
    result_2 = sol.mergeTwoLists1(l1_head, l2_head)

    # print(f"Test Case 1: {l1}, {l2}")
    # print(f"Maximum Subarray Sum: {result_2}\n")  

    # current = l2_head
    # while current:
    #     print(current.value)
    #     current = current.next  
