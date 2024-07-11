# 437 路径总和 III
# https://leetcode.cn/problems/path-sum-iii/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 用前缀和 + 哈希表的方法
# 节点 i 到节点 j 的路径
# v = 根到 j 的和
# ans += v - targetSum 的数量
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node: Optional[TreeNode], pre_sum: int) -> None:
            if not node:
                return
            nonlocal ans
            v = pre_sum + node.val
            ans += cnt[v - targetSum]
            cnt[v] += 1
            dfs(node.left, v)
            dfs(node.right, v)
            cnt[v] -= 1

        cnt = defaultdict(int)
        cnt[0] = 1
        ans = 0
        dfs(root, 0)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
