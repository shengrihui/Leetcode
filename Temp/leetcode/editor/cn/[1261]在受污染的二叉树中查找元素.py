# 1261 在受污染的二叉树中查找元素
# https://leetcode.cn/problems/find-elements-in-a-contaminated-binary-tree/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.nums = set()
        self.f(root, 0)

    def f(self, root: Optional[TreeNode], x: int) -> None:
        if not root:
            return
        self.nums.add(x)
        self.f(root.left, 2 * x + 1)
        self.f(root.right, 2 * x + 2)

    def find(self, target: int) -> bool:
        return target in self.nums

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# leetcode submit region end(Prohibit modification and deletion)
