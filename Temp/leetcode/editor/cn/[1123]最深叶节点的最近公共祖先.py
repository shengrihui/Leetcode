# 1123 最深叶节点的最近公共祖先
# https://leetcode.cn/problems/lowest-common-ancestor-of-deepest-leaves/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 执行耗时:56 ms,击败了66.30% 的Python3用户
# 内存消耗:16.6 MB,击败了33.58% 的Python3用户
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root: Optional[TreeNode], depth: int) -> None:
            if not root:
                return None
            nonlocal mx_depth, leaves
            if depth > mx_depth:
                mx_depth = depth
                leaves = [root]
            elif depth == mx_depth:
                leaves.append(root)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        mx_depth, leaves = 0, []
        dfs(root, 0)
        ans = leaves[0]
        for i in range(1, len(leaves)):
            ans = self.lowestCommonAncestor(root, ans, leaves[i])
        return ans


"""
# 执行耗时:52 ms,击败了84.11% 的Python3用户
# 内存消耗:16.6 MB,击败了35.87% 的Python3用户
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans, mx_depth = None, 0

        # 返回 node 子树的最大深度
        # 如果左子树的深度和右子树的深度一样，那么 当前节点 就是最深根的最近公共祖先
        # 更新 ans
        def dfs(node: Optional[TreeNode], depth: int) -> int:
            nonlocal ans, mx_depth
            if not node:
                mx_depth = max(mx_depth, depth - 1)
                return depth - 1
            left_depth = dfs(node.left, depth + 1)
            right_depth = dfs(node.right, depth + 1)
            if left_depth == right_depth == mx_depth:
                ans = node
            return max(left_depth, right_depth)

        dfs(root, 0)
        return ans
"""

"""
# 执行耗时:76 ms,击败了6.37% 的Python3用户
# 内存消耗:16.7 MB,击败了28.17% 的Python3用户
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 返回 node 这个子树的高度 和 这个子树的“答案”
        # 如果 node 的左子树更高，node子树 的lca 在左子树
        # 如果左右一样高，node 是lca
        def dfs(node: Optional[TreeNode]) -> (int, Optional[TreeNode]):
            if not node:
                return 0, None
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)
            if left_depth > right_depth:
                return left_depth + 1, left_lca
            if right_depth > left_depth:
                return right_depth + 1, right_lca
            return left_depth + 1, node

        return dfs(root)[1]
"""
# leetcode submit region end(Prohibit modification and deletion)
