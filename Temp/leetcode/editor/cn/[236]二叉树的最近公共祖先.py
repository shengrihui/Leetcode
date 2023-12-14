# 236 二叉树的最近公共祖先
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 当前节点 root 如果是 p或q ，那么 root 就是 p和q 的最近公共祖先
# 递归 左/右子树，
# 如果 p q 都在 左/右子树，那么左右子树会返回一个节点，另一边会返回 None
# 如果 p q 分别在 左/右子树，那么左右子树都会会返回一个节点，p和q 的最近公共祖先就是当前节点
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        return right
# leetcode submit region end(Prohibit modification and deletion)
