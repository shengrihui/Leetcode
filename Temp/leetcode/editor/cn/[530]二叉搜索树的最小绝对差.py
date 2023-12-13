# 530 二叉搜索树的最小绝对差
# https://leetcode.cn/problems/minimum-absolute-difference-in-bst/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans, pre = inf, -inf

        def mid(root: Optional[TreeNode]) -> None:
            nonlocal ans, pre
            if not root:
                return None
            mid(root.left)
            x = root.val
            ans = min(ans, x - pre)
            pre = x
            mid(root.right)

        mid(root)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
