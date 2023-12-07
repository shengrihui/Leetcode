# 142 环形链表 II
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 设 head 到环的入口是 a，
        # 入口到相遇点长度是 b，
        # 相遇点到入口是 c，
        # 环长度 b+c
        # 快指针走的是慢指针的两倍，2(a+b)=a+b+k(b+c)
        # 2(a+b)=a+b+b+c+(k-1)(b+c)
        # a-c=(k-1)(b+c)
        # 这意味着，让慢指针和 head 都走 c 步，慢指针到了环的入口，之后两个一起走
        # 一定会相遇，相遇点就是环入口
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                while slow is not head:
                    slow = slow.next
                    head = head.next
                return slow
        return None
# leetcode submit region end(Prohibit modification and deletion)
