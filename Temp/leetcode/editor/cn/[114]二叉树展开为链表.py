# 114 二叉树展开为链表
# https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node = root
        while node:
            if node.left:
                predecessor = node.left
                while predecessor.left or predecessor.right:
                    if predecessor.right:
                        predecessor = predecessor.right
                    else:
                        predecessor = predecessor.left
                predecessor.right = node.right
                node.right = node.left
                t = node
                node = node.left
                t.left = None
            else:
                node = node.right
# leetcode submit region end(Prohibit modification and deletion)
