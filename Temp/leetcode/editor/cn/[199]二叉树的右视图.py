# 199 二叉树的右视图
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
    def dfs(self, root: Optional[TreeNode], depth: int) -> None:
        if root is None:
            return
        if depth > len(self.ans):
            self.ans.append(root.val)
        if root.right:
            self.dfs(root.right, depth + 1)
        if root.left:
            self.dfs(root.left, depth + 1)

    def bfs(self, root: Optional[TreeNode]) -> None:
        q = deque()
        if root:
            q.append((root, 1))
        while q:
            node, depth = q.popleft()
            if depth > len(self.ans):
                self.ans.append(node.val)
            if node.right:
                q.append((node.right, depth + 1))
            if node.left:
                q.append((node.left, depth + 1))

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        # self.dfs(root, 1)
        self.bfs(root)
        return self.ans
# leetcode submit region end(Prohibit modification and deletion)


# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
#  
# 
#  示例 2: 
# 
#  
# 输入: [1,null,3]
# 输出: [1,3]
#  
# 
#  示例 3: 
# 
#  
# 输入: []
# 输出: []
#  
# 
#  
# 
#  提示: 
# 
#  
#  二叉树的节点个数的范围是 [0,100] 
#  
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 999 👎 0
