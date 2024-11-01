# 2236 判断根结点是否等于子结点之和
# https://leetcode.cn/problems/root-equals-sum-of-children/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val
# leetcode submit region end(Prohibit modification and deletion)
