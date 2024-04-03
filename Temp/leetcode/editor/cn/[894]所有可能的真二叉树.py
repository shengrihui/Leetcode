# 894 所有可能的真二叉树
# https://leetcode.cn/problems/all-possible-full-binary-trees/


from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    @cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode()]
        ret = []
        for l in range(1, n, 2):
            left_trees = self.allPossibleFBT(l)
            right_trees = self.allPossibleFBT(n - 1 - l)
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(left=left, right=right)
                    ret.append(root)
        return ret


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.allPossibleFBT(7))
