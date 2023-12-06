# 110 平衡二叉树
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque()
        q.append((root, 0))
        depth = 0
        while q:
            size = 0
            while q and q[0][1] == depth:
                node, d = q.popleft()
                size += 1
                if node.left:
                    q.append((node.left, d + 1))
                if node.right:
                    q.append((node.right, d + 1))
            if pow(2, depth) > size and q:
                return False
            depth += 1
        return True
# leetcode submit region end(Prohibit modification and deletion)


# 给定一个二叉树，判断它是否是高度平衡的二叉树。 
# 
#  本题中，一棵高度平衡二叉树定义为： 
# 
#  
#  一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。 
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：root = []
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中的节点数在范围 [0, 5000] 内 
#  -10⁴ <= Node.val <= 10⁴ 
#  
# 
#  Related Topics 树 深度优先搜索 二叉树 👍 1457 👎 0
