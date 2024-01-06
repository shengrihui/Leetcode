# 2807 在链表中插入最大公约数
# https://leetcode.cn/problems/insert-greatest-common-divisors-in-linked-list/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p and p.next:
            nxt = p.next
            node = ListNode(val=gcd(p.val, nxt.val), next=nxt)
            p.next = node
            p = nxt
        return head
# leetcode submit region end(Prohibit modification and deletion)
