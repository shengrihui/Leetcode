# 92 反转链表 II
from typing import *
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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        p0 = dummy  # 开始翻转区间的前一个
        # 让 p0 到 left 的前一个
        for _ in range(left-1):
            p0 = p0.next

        cur = p0.next
        pre = p0
        nxt = None
        for _ in range(left, right + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        p0.next.next = cur
        p0.next = pre
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)


# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链
# 表节点，返回 反转后的链表 。
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目为 n 
#  1 <= n <= 500 
#  -500 <= Node.val <= 500 
#  1 <= left <= right <= n 
#  
# 
#  
# 
#  进阶： 你可以使用一趟扫描完成反转吗？ 
# 
#  Related Topics 链表 👍 1691 👎 0
