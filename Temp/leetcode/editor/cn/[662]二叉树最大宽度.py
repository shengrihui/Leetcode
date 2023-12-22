# 662 二叉树最大宽度
# https://leetcode.cn/problems/maximum-width-of-binary-tree/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS
    # def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     # 利用满二叉树父子节点编号的性质
    #     # 左=父*2 右=父*2+1
    #     q = deque([(root, 1)])
    #     ans = 1
    #     while q:
    #         ans = max(q[-1][1] - q[0][1] + 1, ans)
    #         for _ in range(len(q)):
    #             node, idx = q.popleft()
    #             if node.left:
    #                 q.append((node.left, idx * 2))
    #             if node.right:
    #                 q.append((node.right, idx * 2 + 1))
    #     return ans

    # DFS
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levelMIn = {}  # 每一层的最小编号

        def dfs(root: Optional[TreeNode], depth: int, index: int) -> int:
            # 当前节点，当前深度，当前节点的编号
            # 返回当前节点为根的最大宽度
            if not root:
                return 0
            if depth not in levelMIn:
                levelMIn[depth] = index
            # 1.当前节点是最右边节点的话宽度；2.递归左右子树
            return max(index - levelMIn[depth] + 1,
                       dfs(root.left, depth + 1, index * 2),
                       dfs(root.right, depth + 1, index * 2 + 1))

        return dfs(root, 1, 1)
# leetcode submit region end(Prohibit modification and deletion)
