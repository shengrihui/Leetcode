# 143 重排链表
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
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 把所有节点都记录下来，然后用两个指针移动来“头插”
        # 最后一定要让最后一个节点的 next 指向空
        nodes = []
        p = head
        while p:
            nodes.append(p)
            p = p.next
        i, j = 1, len(nodes) - 1
        p = head
        while i <= j:
            p.next = nodes[j]
            j -= 1
            p = p.next
            if i < j:
                p.next = nodes[i]
                i += 1
                p = p.next
        p.next = None
'''


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 快慢指针找到链表的中间
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # 将后面一般的反转
        head2 = self.reverseList(slow)
        # 现在有两个节点指向 slow
        # 一个是原本的 slow 的上一个，一个是原本的下一个现在反转后也指向 slow
        # 所以在循环的最后一步，不管两个链表数量是否一样都没有问题
        while head2.next:
            nxt, nxt2 = head.next, head2.next
            head.next = head2
            head2.next = nxt
            head = nxt
            head2 = nxt2

# leetcode submit region end(Prohibit modification and deletion)


# 给定一个单链表 L 的头节点 head ，单链表 L 表示为： 
# 
#  
# L0 → L1 → … → Ln - 1 → Ln
#  
# 
#  请将其重新排列后变为： 
# 
#  
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → … 
# 
#  不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：head = [1,2,3,4]
# 输出：[1,4,2,3] 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：head = [1,2,3,4,5]
# 输出：[1,5,2,4,3] 
# 
#  
# 
#  提示： 
# 
#  
#  链表的长度范围为 [1, 5 * 10⁴] 
#  1 <= node.val <= 1000 
#  
# 
#  Related Topics 栈 递归 链表 双指针 👍 1411 👎 0
