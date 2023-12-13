# 95 不同的二叉搜索树 II
# https://leetcode.cn/problems/unique-binary-search-trees-ii/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]
            ans = []
            for rOOT in range(start, end + 1):  # 枚举不同的根的情况
                leftTrees = dfs(start, rOOT - 1)  # 以 r 为根左子树的情况集合
                rightTrees = dfs(rOOT + 1, end)
                for left in leftTrees:
                    for right in rightTrees:
                        ans.append(TreeNode(val=rOOT, left=left, right=right))
            return ans

        return dfs(1, n)
# leetcode submit region end(Prohibit modification and deletion)
