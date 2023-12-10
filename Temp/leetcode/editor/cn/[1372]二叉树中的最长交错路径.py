# 1372 二叉树中的最长交错路径
# https://leetcode.cn/problems/longest-zigzag-path-in-a-binary-tree/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], s: int, from_r: bool) -> None:
            # s：到 node 的路径的节点个数 = 长度+1
            # from_r：上一步是不是 向右走的
            nonlocal ans
            if node is None:  # 空节点
                return
            ans = max(ans, s - 1)
            # 因为前面会判断是不是空节点，所以不用 if node.left/right，直接下去，如果是空回直接 return
            if from_r:  # 当前这个节点是从父节点那里 向右 来的
                dfs(node.left, s + 1, False)  # 下一步向左，s 累积
                dfs(node.right, 2, True)  # 下一步仍然向右，s 重置，到子节点，路径上的节点数是2了
            else:
                dfs(node.right, s + 1, True)
                dfs(node.left, 2, False)

        ans = 0
        dfs(root, 1, False)
        dfs(root, 1, True)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
