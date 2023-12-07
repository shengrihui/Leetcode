# 876 链表的中间结点
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
# leetcode submit region end(Prohibit modification and deletion)


# 给你单链表的头结点 head ，请你找出并返回链表的中间结点。 
# 
#  如果有两个中间结点，则返回第二个中间结点。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,2,3,4,5]
# 输出：[3,4,5]
# 解释：链表只有一个中间结点，值为 3 。
#  
# 
#  示例 2： 
#  
#  
# 输入：head = [1,2,3,4,5,6]
# 输出：[4,5,6]
# 解释：该链表有两个中间结点，值分别为 3 和 4 ，返回第二个结点。
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表的结点数范围是 [1, 100] 
#  1 <= Node.val <= 100 
#  
# 
#  Related Topics 链表 双指针 👍 960 👎 0
