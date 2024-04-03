# 1379 找出克隆二叉树中的相同节点
# https://leetcode.cn/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        if original == target:
            return cloned
        left = self.getTargetCopy(original.left, cloned.left, target)
        if left:
            return left
        return self.getTargetCopy(original.right, cloned.right, target)

# leetcode submit region end(Prohibit modification and deletion)
