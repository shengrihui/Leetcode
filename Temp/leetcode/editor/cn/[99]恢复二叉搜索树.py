# 99 恢复二叉搜索树
# https://leetcode.cn/problems/recover-binary-search-tree/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def mid_travel(node: Optional[TreeNode]) -> None:
            nonlocal err1, err2, a, b
            if not node:
                return
            mid_travel(node.left)
            a, b = b, node
            if a and b and a.val > b.val:
                if not err1:
                    err1, err2 = a, b
                else:
                    err2 = b
            mid_travel(node.right)

        a, b = None, None
        err1, err2 = None, None
        mid_travel(root)
        err1.val, err2.val = err2.val, err1.val
# leetcode submit region end(Prohibit modification and deletion)
