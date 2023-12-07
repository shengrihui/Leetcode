# 24 两两交换链表中的节点
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        n = 0
        p = head
        while p is not None:
            n += 1
            p = p.next
        p = dummy  # 反转区间的前一个
        for _ in range(n // k):
            cur = p.next
            pre = p
            for i in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            # cur 到了下一个区间的第一个
            t = p.next  # 现在 p 的 next 还是一开始区间的第一个，也就是下一个区间的前一个
            p.next.next = cur  # ，将它的 next 指向下一个区间的第一个，也就是 cur
            p.next = pre
            p = t
        return dummy.next

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseKGroup(head, 2)
# leetcode submit region end(Prohibit modification and deletion)


# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1]
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 100] 内 
#  0 <= Node.val <= 100 
#  
# 
#  Related Topics 递归 链表 👍 2097 👎 0
