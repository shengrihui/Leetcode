# 257 二叉树的所有路径
from collections import *
from typing import List, Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], path: List[int]) -> None:
        if not root.right and not root.left:
            path.append(root.val)
            self.ans.append("->".join(map(str, path)))
            return
        if root.left:
            self.dfs(root.left, path + [root.val])
        if root.right:
            self.dfs(root.right, path + [root.val])

    def bfs(self, root: Optional[TreeNode]) -> None:
        q = deque([(root, [root.val])])
        while q:
            node, path = q.popleft()
            if not node.right and not node.left:
                self.ans.append("->".join(map(str, path)))
            if node.left:
                q.append((node.left, path + [node.left.val]))
            if node.right:
                q.append((node.right, path + [node.right.val]))

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []
        # self.dfs(root, [])
        self.bfs(root)
        return self.ans
# leetcode submit region end(Prohibit modification and deletion)


# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。 
# 
#  叶子节点 是指没有子节点的节点。 
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,3,null,5]
# 输出：["1->2->5","1->3"]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [1]
# 输出：["1"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目在范围 [1, 100] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics 树 深度优先搜索 字符串 回溯 二叉树 👍 1072 👎 0
