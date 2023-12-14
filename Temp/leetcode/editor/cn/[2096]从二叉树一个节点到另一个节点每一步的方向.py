# 2096 从二叉树一个节点到另一个节点每一步的方向
# https://leetcode.cn/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(root: Optional[TreeNode]) -> None:
            if not root:
                return
            nonlocal d, path
            if root.val in [startValue, destValue]:
                d[root.val] = path.copy()
                if len(d) == 2:
                    return
            path.append("L")
            dfs(root.left)
            path[-1] = "R"
            dfs(root.right)
            path.pop()

        d, path = {}, []
        dfs(root)
        # 找出从根节点到 s 和 t 的路径共同的长度
        i = 0
        n, m = len(d[startValue]), len(d[destValue])
        while i < n and i < m and d[startValue][i] == d[destValue][i]:
            i += 1
        #      s 到 公共祖先都是 U + t 路径去掉公共部分
        return "U" * (n - i) + "".join(d[destValue][i:])

# leetcode submit region end(Prohibit modification and deletion)
