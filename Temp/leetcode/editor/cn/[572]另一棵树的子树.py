# 572 另一棵树的子树
# https://leetcode.cn/problems/subtree-of-another-tree/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
            if not s and not t:
                return True
            if s and not t or not s and t:
                return False
            return s.val == t.val and check(s.left, t.left) and check(s.right, t.right)

        def dfs(root: Optional[TreeNode]) -> bool:
            if not root:
                return False
            if root.val == subRoot.val:
                if check(root, subRoot):
                    return True
            if dfs(root.left) or dfs(root.right):
                return True
            return False

        return dfs(root)
# leetcode submit region end(Prohibit modification and deletion)
