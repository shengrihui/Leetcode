# 445 两数相加 II
from typing import Optional


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

    def addNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode()
        p = ret
        c = 0
        while l1 or l2 or c:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + c
            t = ListNode(s % 10)
            c = s // 10
            p.next = t
            p = p.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return ret.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        r = self.addNumbers(l1, l2)
        return self.reverseList(r)
# leetcode submit region end(Prohibit modification and deletion)


# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。 
# 
#  你可以假设除了数字 0 之外，这两个数字都不会以零开头。 
# 
#  
# 
#  示例1： 
# 
#  
# 
#  
# 输入：l1 = [7,2,4,3], l2 = [5,6,4]
# 输出：[7,8,0,7]
#  
# 
#  示例2： 
# 
#  
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[8,0,7]
#  
# 
#  示例3： 
# 
#  
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表的长度范围为 [1, 100] 
#  0 <= node.val <= 9 
#  输入数据保证链表代表的数字无前导 0 
#  
# 
#  
# 
#  进阶：如果输入链表不能翻转该如何解决？ 
# 
#  Related Topics 栈 链表 数学 👍 691 👎 0
