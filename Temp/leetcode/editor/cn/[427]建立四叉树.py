# 427 建立四叉树
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(x0: int, y0: int, x1: int, y1: int) -> 'Node':
            if x0 == x1:
                return Node(grid[x0][y0], True, None, None, None, None, )
            ok = True
            t = grid[x0][y0]
            for i in range(x0, x1 + 1):
                for j in range(y0, y1 + 1):
                    if grid[i][j] != t:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                return Node(t, True, None, None, None, None)
            node = Node(t, False, None, None, None, None)
            m = (x1 - x0 + 1) // 2
            node.topLeft = dfs(x0, y0, x1 - m, y1 - m)
            node.topRight = dfs(x0, y0 + m, x1 - m, y1)
            node.bottomLeft = dfs(x0 + m, y0, x1, y1 - m)
            node.bottomRight = dfs(x0 + m, y0 + m, x1, y1)
            return node

        n = len(grid)
        return dfs(0, 0, n - 1, n - 1)
# leetcode submit region end(Prohibit modification and deletion)


# 给你一个 n * n 矩阵 grid ，矩阵由若干 0 和 1 组成。请你用四叉树表示该矩阵 grid 。 
# 
#  你需要返回能表示矩阵 grid 的 四叉树 的根结点。 
# 
#  四叉树数据结构中，每个内部节点只有四个子节点。此外，每个节点都有两个属性： 
# 
#  
#  val：储存叶子结点所代表的区域的值。1 对应 True，0 对应 False。注意，当 isLeaf 为 False 时，你可以把 True 或者 
# False 赋值给节点，两种值都会被判题机制 接受 。 
#  isLeaf: 当这个节点是一个叶子结点时为 True，如果它有 4 个子节点则为 False 。 
#  
# 
#  
# class Node {
#     public boolean val;
#     public boolean isLeaf;
#     public Node topLeft;
#     public Node topRight;
#     public Node bottomLeft;
#     public Node bottomRight;
# } 
# 
#  我们可以按以下步骤为二维区域构建四叉树： 
# 
#  
#  如果当前网格的值相同（即，全为 0 或者全为 1），将 isLeaf 设为 True ，将 val 设为网格相应的值，并将四个子节点都设为 Null 然后
# 停止。 
#  如果当前网格的值不同，将 isLeaf 设为 False， 将 val 设为任意值，然后如下图所示，将当前网格划分为四个子网格。 
#  使用适当的子网格递归每个子节点。 
#  
# 
#  
# 
#  如果你想了解更多关于四叉树的内容，可以参考 wiki 。 
# 
#  四叉树格式： 
# 
#  你不需要阅读本节来解决这个问题。只有当你想了解输出格式时才会这样做。输出为使用层序遍历后四叉树的序列化形式，其中 null 表示路径终止符，其下面不存在节
# 点。 
# 
#  它与二叉树的序列化非常相似。唯一的区别是节点以列表形式表示 [isLeaf, val] 。 
# 
#  如果 isLeaf 或者 val 的值为 True ，则表示它在列表 [isLeaf, val] 中的值为 1 ；如果 isLeaf 或者 val 的值为
#  False ，则表示值为 0 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：grid = [[0,1],[1,0]]
# 输出：[[0,1],[1,0],[1,1],[1,1],[1,0]]
# 解释：此示例的解释如下：
# 请注意，在下面四叉树的图示中，0 表示 false，1 表示 True 。
# 
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,
# 1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
# 输出：[[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
# 
# 解释：网格中的所有值都不相同。我们将网格划分为四个子网格。
# topLeft，bottomLeft 和 bottomRight 均具有相同的值。
# topRight 具有不同的值，因此我们将其再分为 4 个子网格，这样每个子网格都具有相同的值。
# 解释如下图所示：
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == grid.length == grid[i].length 
#  n == 2ˣ 其中 0 <= x <= 6 
#  
# 
#  Related Topics 树 数组 分治 矩阵 👍 201 👎 0
