# 104 二叉树的最大深度
# https://leetcode.cn/problems/maximum-depth-of-binary-tree/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # else:
        #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        if not root:
            return 0
        depth = 0
        q = deque()
        q.append((root, depth + 1))
        while q:
            node, depth = q.popleft()
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
        return depth
# leetcode submit region end(Prohibit modification and deletion)
