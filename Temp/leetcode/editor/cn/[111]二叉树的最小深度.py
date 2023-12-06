# 111 二叉树的最小深度
from typing import List, Optional
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


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


# 给定一个二叉树，找出其最小深度。 
# 
#  最小深度是从根节点到最近叶子节点的最短路径上的节点数量。 
# 
#  说明：叶子节点是指没有子节点的节点。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [2,null,3,null,4,null,5,null,6]
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数的范围在 [0, 10⁵] 内 
#  -1000 <= Node.val <= 1000 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1131 👎 0
