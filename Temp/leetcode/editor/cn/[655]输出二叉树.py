# 655 输出二叉树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def row(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.row(root.left), self.row(root.right))

    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = self.row(root) - 1
        cols = pow(2, height + 1) - 1
        res = [[""] * cols for _ in range(height + 1)]

        def dfs(node: Optional[TreeNode], ro: int, col: int) -> None:
            nonlocal res
            res[ro][col] = str(node.val)
            d = pow(2, height - ro - 1)
            if node.left:
                dfs(node.left, ro + 1, col - d)
            if node.right:
                dfs(node.right, ro + 1, col + d)

        dfs(root, 0, (cols - 1) // 2)
        return res
# leetcode submit region end(Prohibit modification and deletion)
