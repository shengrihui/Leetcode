# 23 合并 K 个升序链表
import heapq
from typing import *


# 分治
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        prev = head
        # prev指向当前已经合并了的最后一个节点
        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next  # 记得更新prev
        prev.next = list1 if list1 is not None else list2
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        l1 = self.mergeKLists(lists[:n // 2])
        l2 = self.mergeKLists(lists[n // 2:])
        return self.mergeTwoLists(l1, l2)


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


ListNode.__lt__ = lambda a, b: a.val < b.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = [node for node in lists if node is not None]
        heapq.heapify(q)
        head = cur = ListNode(-1)
        while q:
            node = heapq.heappop(q)
            cur.next = node
            if node.next is not None:
                heapq.heappush(q, node.next)
            cur = cur.next
        return head.next

# leetcode submit region end(Prohibit modification and deletion)
