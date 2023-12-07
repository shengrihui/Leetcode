# 113 路径总和 II
from collections import *
from typing import List, Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], targetSum: int) -> None:
        v = root.val
        self.path.append(v)
        if not root.left and not root.right and v == targetSum:
            self.ans.append(self.path.copy())  # copy!!!
            return
        if root.left:
            self.dfs(root.left, targetSum - v)
            self.path.pop()
        if root.right:
            self.dfs(root.right, targetSum - v)
            self.path.pop()

    def bfs(self, root: Optional[TreeNode], targetSum: int) -> None:
        q = deque()
        q.append((root, [root.val]))
        while q:
            node, path = q.popleft()
            if not node.left and not node.right:
                if sum(path) == targetSum:
                    self.ans.append(path)
            if node.left:
                q.append((node.left, path + [node.left.val]))
            if node.right:
                q.append((node.right, path + [node.right.val]))

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self.ans = []
        self.path = []
        # self.dfs(root, targetSum)
        self.bfs(root, targetSum)
        return self.ans
# leetcode submit region end(Prohibit modification and deletion)
