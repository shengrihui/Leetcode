# 2385 感染二叉树需要的总时间
# https://leetcode.cn/problems/amount-of-time-for-binary-tree-to-be-infected/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(root: Optional[TreeNode], fa: int) -> None:
            x = root.val
            if fa != -1:
                g[x].append(fa)
            if root.left:
                g[x].append(root.left.val)
                dfs(root.left, x)
            if root.right:
                g[x].append(root.right.val)
                dfs(root.right, x)

        g = defaultdict(list)
        dfs(root, -1)
        ans = 0
        q = deque([start])
        vis = {start}
        while q:
            for _ in range(len(q)):
                x = q.popleft()
                for y in g[x]:
                    if y not in vis:
                        q.append(y)
                        vis.add(y)
            ans += 1
        return ans - 1


"""
# 灵神
Class Solution:
"""
# leetcode submit region end(Prohibit modification and deletion)
