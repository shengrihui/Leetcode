# 993 二叉树的堂兄弟节点
# https://leetcode.cn/problems/cousins-in-binary-tree/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque()
        q.append(root)
        while q:
            tmp = None
            for _ in range(len(q)):
                node = q.popleft()
                for n in [node.left, node.right]:
                    if n:
                        q.append(n)
                        if n.val in [x, y]:
                            if tmp == node:  # x,y 相同的父节点
                                return False
                            if tmp:
                                return True
                            tmp = node
        return False
# leetcode submit region end(Prohibit modification and deletion)
