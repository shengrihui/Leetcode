# 98 验证二叉搜索树
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        a = -inf

        def midTrace(node) -> bool:
            nonlocal a
            if node.left and not midTrace(node.left):
                return False
            if node.val <= a:
                return False
            a = node.val
            if node.right and not midTrace(node.right):
                return False
            return True

        return midTrace(root)
# leetcode submit region end(Prohibit modification and deletion)
