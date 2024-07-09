# 437 路径总和 III
# https://leetcode.cn/problems/path-sum-iii/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node: Optional[TreeNode], s: int) -> None:
            if not node:
                return
            v = s + node.val
            if v == targetSum:
                nonlocal ans
                print(s, node.val, node)
                ans += 1
            # print(node.val, "left", v)
            # dfs(node.left, v)
            # print(node.val, "left", 0)
            # dfs(node.left, 0)
            print(node.val, "r", v)
            dfs(node.right, v)
            print(node.val, "r", 0)
            dfs(node.right, 0)

        ans = 0
        dfs(root, 0)
        print()
        return ans
# leetcode submit region end(Prohibit modification and deletion)
