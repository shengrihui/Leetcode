# 103 二叉树的锯齿形层序遍历
# https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# LCR 151
# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         ans = []
#         row, nxt = 0, 1  # 当前行，下一行
#         qs = [deque(), deque()]
#         if root:
#             qs[row].append(root)
#         while qs[row]:
#             row_record = []
#             while qs[row]:
#                 if row & 1 == 0:  # 从左往右读，在 nxt 右边加入
#                     node = qs[row].popleft()
#                     if node.left: qs[nxt].append(node.left)
#                     if node.right: qs[nxt].append(node.right)
#                 else:  # 从右往左读，在 nxt 左边加入
#                     node = qs[row].pop()
#                     if node.right: qs[nxt].appendleft(node.right)
#                     if node.left: qs[nxt].appendleft(node.left)
#                 row_record.append(node.val)
#             ans.append(row_record)
#             row, nxt = nxt, row
#         return ans

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque()
        if root:
            q.append(root)
        even = True  # 偶数层
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(vals if even else vals[::-1])
            even = not even
        return ans

# leetcode submit region end(Prohibit modification and deletion)
