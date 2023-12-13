# 230 二叉搜索树中第K小的元素
# https://leetcode.cn/problems/kth-smallest-element-in-a-bst/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0

        def mid(root: Optional[TreeNode]) -> int:
            if not root:
                return inf
            l = mid(root.left)
            if l != inf:
                return l
            nonlocal cnt
            cnt += 1
            if cnt == k:
                return root.val
            return mid(root.right)

        return mid(root)

# leetcode submit region end(Prohibit modification and deletion)
