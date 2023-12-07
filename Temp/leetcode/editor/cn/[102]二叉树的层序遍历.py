# 102 二叉树的层序遍历
from collections import *
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque()
        q.append(root)
        while q:
            sz = len(q)
            row = []
            for _ in range(sz):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                row.append(node.val)
            ans.append(row)
        return ans

# leetcode submit region end(Prohibit modification and deletion)


