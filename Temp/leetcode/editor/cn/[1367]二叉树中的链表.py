# 1367 二叉树中的链表
# https://leetcode.cn/problems/linked-list-in-binary-tree/
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

# https://leetcode.cn/problems/linked-list-in-binary-tree/solutions/122916/er-cha-shu-zhong-de-lie-biao-by-leetcode-solution
class Solution:
    # 就以 root 为根作为链头开始进行比较
    def dfs(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False
        if head.val != root.val:
            return False
        return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
# leetcode submit region end(Prohibit modification and deletion)
