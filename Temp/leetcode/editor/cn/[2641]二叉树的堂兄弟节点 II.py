# 2641 二叉树的堂兄弟节点 II
# https://leetcode.cn/problems/cousins-in-binary-tree-ii/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        d = defaultdict(int)
        row_sum = []
        q.append(root)
        while q:
            s = 0
            for _ in range(len(q)):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                    d[node.left] += node.left.val
                    d[node.right] += node.left.val
                if node.right:
                    q.append(node.right)
                    d[node.left] += node.right.val
                    d[node.right] += node.right.val
            row_sum.append(s)

        q.append(root)
        row = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                node.val = row_sum[row] - d[node]
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            row += 1
        root.val = 0
        return root
# leetcode submit region end(Prohibit modification and deletion)
