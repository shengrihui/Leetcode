# 111 二叉树的最小深度
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def minDepth(self, root: Optional[TreeNode]) -> int:
    #     def f(node: Optional[TreeNode], cnt: int) -> None:
    #         if not node:
    #             return
    #         if not node.left and not node.right:
    #             nonlocal ans
    #             ans = min(ans, cnt)
    #             return
    #         f(node.left, cnt + 1)
    #         f(node.right, cnt + 1)
    #
    #     ans = inf
    #     f(root, 1)
    #     return ans if ans != inf else 0
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # 如果左子树是空或者右子树是空，那两者较小值就是 0 了
        m1 = self.minDepth(root.left)
        m2 = self.minDepth(root.right)
        return 1 + (min(m1, m2) if root.left and root.right else m1 + m2)
# leetcode submit region end(Prohibit modification and deletion)


