# 143 重排链表
from typing import Optional

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
