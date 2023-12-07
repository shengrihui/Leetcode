# 129 求根节点到叶节点数字之和
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal ans, s
            s = s * 10 + root.val
            if not root.left and not root.right:
                ans += s
                return
            if root.left:
                dfs(root.left)
                s //= 10
            if root.right:
                dfs(root.right)
                s //= 10

        ans = 0
        s = 0
        dfs(root)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
