# 671 二叉树中第二小的节点
# https://leetcode.cn/problems/second-minimum-node-in-a-binary-tree/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root.right:
            return -1
        mn = root.val
        # 如果左儿子和根值相同，那么左儿子的值是左子树（也是整个树）的最小，不是的第二小的，递归去找
        # 如果不同，那么左儿子的值（左子树的最小值），就有可能是 root 树的第二小值
        left = root.left.val if root.left.val != mn else self.findSecondMinimumValue(root.left)
        right = root.right.val if root.right.val != mn else self.findSecondMinimumValue(root.right)
        # left right 分别两个可能是 root 为根的树的第二小值
        # 如果有一个是 -1 ，返回二者的较大值
        # 否则返回二者的较小值，它就是 root 这个子树的第二小值（最小是 root.val)
        return min(left, right) if left != -1 and right != -1 else max(left, right)
# leetcode submit region end(Prohibit modification and deletion)
