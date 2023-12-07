# 1026 节点与其祖先之间的最大差值
# https://leetcode.cn/problems/maximum-difference-between-node-and-ancestor/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def f(node, mx, mn):
            if node.left is None and node.right is None:
                nonlocal ans
                ans = max(ans, mx - mn)
            if node.left:
                f(node.left, max(mx, node.left.val), min(mn, node.left.val))
            if node.right:
                f(node.right, max(mx, node.right.val), min(mn, node.right.val))

        ans = 0
        f(root, root.val, root.val)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
