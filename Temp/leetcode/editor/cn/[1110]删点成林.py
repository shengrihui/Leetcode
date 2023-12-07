# 1110 删点成林
# https://leetcode.cn/problems/delete-nodes-and-return-forest/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 在“归”的时候删除节点，删除的时候将该节点的左右孩子（如果不为空）加入答案列表
    # 递归函数返回这个节点的结局：被删除了，返回 None；没被删除，返回本身。
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val in to_delete:
                nonlocal ans
                if node.left:
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)
                return None
            return node

        ans = []
        to_delete.append(-1)
        dummy = TreeNode(val=-1, left=root)
        dfs(dummy)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
