# 2583 二叉树中的第 K 大层和
# https://leetcode.cn/problems/kth-largest-sum-in-a-binary-tree/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        s = []
        while q:
            ss = 0
            for _ in range(len(q)):
                node = q.popleft()
                ss += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            s.append(ss)
        s.sort()
        return s[- k] if len(s) >= k else -1
# leetcode submit region end(Prohibit modification and deletion)
