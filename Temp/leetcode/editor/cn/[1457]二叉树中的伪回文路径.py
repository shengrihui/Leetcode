# 1457 二叉树中的伪回文路径
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def isPalindromic(cnt: List[int]) -> bool:
            odd = False
            for x in cnt:
                if x % 2:
                    if odd:
                        return False
                    odd = True
            return True

        def helper(node: Optional[TreeNode]) -> None:
            nonlocal ans, path
            path[node.val] += 1
            if not node.left and not node.right:
                ans += isPalindromic(path)
                return
            if node.left:
                helper(node.left)
                path[node.left.val] -= 1
            if node.right:
                helper(node.right)
                path[node.right.val] -= 1

        ans = 0
        path = [0] * 10
        helper(root)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
