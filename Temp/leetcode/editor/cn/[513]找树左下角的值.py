# 513 找树左下角的值
# https://leetcode.cn/problems/find-bottom-left-tree-value/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        while q:
            node = q.popleft()
            if node.right: q.append(node.right)
            if node.left: q.append(node.left)
        return node.val


# leetcode submit region end(Prohibit modification and deletion)


print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
