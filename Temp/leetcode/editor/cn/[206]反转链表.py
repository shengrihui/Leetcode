# 206 反转链表
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        q = head
        while q:
            q = head.next
            head.next = new_head.next
            new_head.next = head
            head = q
        return new_head.next

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev = None
#         curr = head
#         while curr:
#             next_ = curr.next  # 找到下一个节点
#             curr.next = prev  # 当前节点指向上一个
#             prev = curr  # 更新上一个
#             curr = next_  # 更新当前，如果时空了也就是最后了
#         return prev  # 退出循环后prev指向最后一个节点，curr和next_都指向空

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:  # 递归退出的条件
#             return head
#         newhead = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return newhead
# leetcode submit region end(Prohibit modification and deletion)
