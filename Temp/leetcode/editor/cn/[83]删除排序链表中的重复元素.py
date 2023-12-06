# 83 删除排序链表中的重复元素
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
        p = head
        while p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:  # 如果不一样了才往后移动
                p = p.next
        return head
# leetcode submit region end(Prohibit modification and deletion)


# 给定一个已排序的链表的头
#  head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,1,2]
# 输出：[1,2]
#  
# 
#  示例 2： 
#  
#  
# 输入：head = [1,1,2,3,3]
# 输出：[1,2,3]
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
#  Related Topics 链表 👍 1073 👎 0
