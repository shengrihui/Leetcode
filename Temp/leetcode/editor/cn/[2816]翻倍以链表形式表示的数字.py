# 2816 翻倍以链表形式表示的数字
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 递归
# class Solution:
#     def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None:  # 递归边界，最后一位的后面，返回一个空的节点
#             return ListNode(0, None)
#         r = self.doubleIt(head.next)
#         # 如果低位有进位，则 c 是进位值
#         # 如果没有进位（返回的就是原本的下一个节点），进位 c 是 0
#         c = 0 if r == head.next else r.val
#         v = head.val * 2 + c
#         head.val = v % 10
#         carry = v // 10
#         return head if carry == 0 else ListNode(carry, head)

# 一次遍历
# 进位只会发生在 下一个数>4 的时候
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val > 4:
            head = ListNode(0, head)
        p = head
        while p:
            p.val = (p.val * 2) % 10
            if p.next and p.next.val > 4:
                p.val += 1
            p = p.next
        return head
# leetcode submit region end(Prohibit modification and deletion)
