# 108 将有序数组转换为二叉搜索树
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def f(l: int, r: int) -> Optional[TreeNode]:
            mid = (l + r) // 2
            node = TreeNode(nums[mid])
            if l == r:
                return node
            if l != mid:
                node.left = f(l, mid - 1)
            node.right = f(mid + 1, r)
            return node

        return f(0, len(nums) - 1)
# leetcode submit region end(Prohibit modification and deletion)


