# 82 删除排序链表中的重复元素 II
from typing import Optional


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
