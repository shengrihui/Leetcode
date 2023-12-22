# 814 二叉树剪枝
# https://leetcode.cn/problems/binary-tree-pruning/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root:Optional[TreeNode])->bool:
            if not root:
                return True
            left=dfs(root.left)
            right=dfs(root.right)
            if left:
                root.left=None
            if right:
                root.right=None
            return left and right and root.val==0
        if dfs(root):
            return None
        return root
# leetcode submit region end(Prohibit modification and deletion)

