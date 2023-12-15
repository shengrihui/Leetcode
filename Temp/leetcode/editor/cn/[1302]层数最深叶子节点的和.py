# 1302 层数最深叶子节点的和
# https://leetcode.cn/problems/deepest-leaves-sum/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], depth: int) -> None:
        if not root:
            return
        if depth == self.mx_depth:
            self.ans += root.val
        elif depth > self.mx_depth:
            self.ans = root.val
            self.mx_depth = depth
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)

    def bfs(self, root: Optional[TreeNode]) -> None:
        q = deque([root])
        while q:
            s = 0
            for _ in range(len(q)):
                node = q.popleft()
                s += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            self.ans = s

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.mx_depth = 0
        # self.dfs(root, 0)
        self.bfs(root)
        return self.ans
# leetcode submit region end(Prohibit modification and deletion)
