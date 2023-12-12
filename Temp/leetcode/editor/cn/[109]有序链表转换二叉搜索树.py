# 109 有序链表转换二叉搜索树
# https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode], tail: Optional[ListNode] = None) -> Optional[TreeNode]:
        if head is tail:  # 这一段为空 [head,tail)
            return None
        slow = fast = head
        while fast is not tail and fast.next is not tail:
            slow = slow.next
            fast = fast.next.next
        return TreeNode(slow.val, self.sortedListToBST(head, slow), self.sortedListToBST(slow.next, tail))
# leetcode submit region end(Prohibit modification and deletion)
