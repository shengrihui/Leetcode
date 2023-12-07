# 124 二叉树中的最大路径和
from math import *
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def f(node: Optional[TreeNode]) -> int:
            nonlocal ans
            v = node.val
            left = right = -inf
            if node.left:
                left = f(node.left) + v
            if node.right:
                right = f(node.right) + v
            ans = max(ans, v, left, right, left + right - v)
            return max(v, left, right)

        ans = -inf
        f(root)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
