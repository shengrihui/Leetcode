# 110 平衡二叉树
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node: Optional[TreeNode]) -> int:
            # 是平衡二叉树，返回高度
            # 不是平衡二叉树，返回-1
            if not node:
                return 0
            left_height = get_height(node.left)
            if left_height == -1:
                return -1
            right_height = get_height(node.right)
            if right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1

        return get_height(root) != -1
# leetcode submit region end(Prohibit modification and deletion)


