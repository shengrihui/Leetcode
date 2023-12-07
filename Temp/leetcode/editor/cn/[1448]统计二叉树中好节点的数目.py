# 1448 统计二叉树中好节点的数目
from collections import *
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], mx: int) -> None:
        if not root:
            return
        if root.val >= mx:
            mx = root.val
            self.ans += 1
        if root.left:
            self.dfs(root.left, mx)
        if root.right:
            self.dfs(root.right, mx)

    def bfs(self, root: Optional[TreeNode]) -> None:
        q = deque([(root, root.val)])
        while q:
            node, mx = q.popleft()
            if not node:
                continue
            if node.val >= mx:
                mx = node.val
                self.ans += 1
            if node.left:
                q.append((node.left, mx))
            if node.right:
                q.append((node.right, mx))

    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        # self.dfs(root, root.val)
        self.bfs(root)
        return self.ans
# leetcode submit region end(Prohibit modification and deletion)
