# 1080 根到叶路径上的不足节点
# https://leetcode.cn/problems/insufficient-nodes-in-root-to-leaf-paths/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
#         def f(node: Optional[TreeNode], s: int) -> bool:
#             if node.left is None and node.right is None:
#                 return s >= limit
#             left_flag = right_flag = False
#             if node.left:
#                 left_flag = f(node.left, s + node.left.val)
#                 if not left_flag:
#                     node.left = None
#             if node.right:
#                 right_flag = f(node.right, s + node.right.val)
#                 if not right_flag:
#                     node.right = None
#             return left_flag or right_flag
#
#         dummy = TreeNode(left=root)
#         if not f(dummy.left, dummy.left.val):
#             dummy.left = None
#         return dummy.left

class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        limit -= root.val
        if root.left is root.right:  # root 是叶子
            # 如果 limit > 0 说明从根到叶子的路径和小于 limit，删除叶子，否则不删除
            return None if limit > 0 else root
        if root.left: root.left = self.sufficientSubset(root.left, limit)
        if root.right: root.right = self.sufficientSubset(root.right, limit)
        # 如果有儿子没被删除，就不删 root，否则删 root
        return root if root.left or root.right else None

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/insufficient-nodes-in-root-to-leaf-paths/solutions/2278769/jian-ji-xie-fa-diao-yong-zi-shen-pythonj-64lf/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# leetcode submit region end(Prohibit modification and deletion)
