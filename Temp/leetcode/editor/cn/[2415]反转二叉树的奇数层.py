# 2415 反转二叉树的奇数层
# https://leetcode.cn/problems/reverse-odd-levels-of-binary-tree/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        row = 0
        while q:
            for _ in range(pow(2, row)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            row += 1
            if row & 1 and q:
                i, j = 0, pow(2, row) - 1
                while i < j:
                    q[i].val, q[j].val = q[j].val, q[i].val
                    i += 1
                    j -= 1
        return root
# leetcode submit region end(Prohibit modification and deletion)
