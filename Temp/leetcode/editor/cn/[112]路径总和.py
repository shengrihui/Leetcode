# 112 路径总和
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def f(node: Optional[TreeNode], s: int) -> bool:
            if not node.left and not node.right:
                return node.val + s == targetSum
            if node.left and f(node.left, s + node.val):
                return True
            if node.right and f(node.right, s + node.val):
                return True
            return False

        return root is not None and f(root, 0)
# leetcode submit region end(Prohibit modification and deletion)
