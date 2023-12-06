# 82 删除排序链表中的重复元素 II
from typing import List, Optional
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(next=head)
        prev = dummy
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                p = cur.next
                while p.next and p.val == p.next.val:
                    p = p.next
                prev.next = p.next
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)


# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
#  
# 
#  示例 2： 
#  
#  
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目在范围 [0, 300] 内 
#  -100 <= Node.val <= 100 
#  题目数据保证链表已经按升序 排列 
#  
# 
#  Related Topics 链表 双指针 👍 1212 👎 0
