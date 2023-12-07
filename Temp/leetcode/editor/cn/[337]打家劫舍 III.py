# 337 打家劫舍 III
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def trace(root):
            if root is None:
                return [0, 0]
            # 放回 [选root节点最大钱数 ，不选root节点最大钱数 ]
            left = trace(root.left)
            right = trace(root.right)
            return [root.val + left[1] + right[1],  # root选，左右只能都不选
                    max(left) + max(right)  # root不选，
                    ]
            # max(left[0] + right[0],  # root不选，
            #     left[0] + right[1],
            #     left[1] + right[0],
            #     left[1] + right[1],
            #     )]

        return max(trace(root))

# leetcode submit region end(Prohibit modification and deletion)
