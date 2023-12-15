# 199 二叉树的右视图
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
        if root is None:
            return
        if depth > len(self.ans):
            self.ans.append(root.val)
        if root.right:
            self.dfs(root.right, depth + 1)
        if root.left:
            self.dfs(root.left, depth + 1)

    def bfs(self, root: Optional[TreeNode]) -> None:
        q = deque()
        if root:
            q.append((root, 1))
        while q:
            node, depth = q.popleft()
            if depth > len(self.ans):
                self.ans.append(node.val)
            if node.right:
                q.append((node.right, depth + 1))
            if node.left:
                q.append((node.left, depth + 1))

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        # self.dfs(root, 1)
        self.bfs(root)
        return self.ans
# leetcode submit region end(Prohibit modification and deletion)
