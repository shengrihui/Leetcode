# 543 二叉树的直径
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def depth(root):
            nonlocal ans
            if not root:
                return 0
            L = depth(root.left)
            R = depth(root.right)
            ans = max(ans, L + R)
            return max(L, R) + 1

        depth(root)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
