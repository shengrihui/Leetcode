# 1483 树节点的第 K 个祖先
# https://leetcode.cn/problems/kth-ancestor-of-a-tree-node/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# 树上倍增算法
# 用 pa[x][i] 表示节点 x 的第 2^i 的祖先是谁
# pa[x][0] = parent[x] 父节点
# pa[x][1] = pa[ parent[x] ][0] 爷爷节点 = 父节点的父节点
# 也就是 pa[x][1] = pa[ pa[x][0] ][0]
# 一般的 pa[x][i] = pa[ pa[x][i-1] ][i]
# i-1 要特殊考虑 0，不要这样，所以
#  pa[x][i+1] = pa[ pa[x][i] ][i]
# 如果这个祖先不存在，那 pa[x][i]（以及更大的 i）= -1
# i 的大小范围与节点的数量有关
# 一个节点最多有 log_{2}^{n}下取整 的 2 的幂次祖先
# 而 log_{2}^{n}下取整 和 n的二进制位数-1 一样

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        m = n.bit_length() - 1
        # m = int(math.log2(n))  # 同上
        # m = (n - 1).bit_length()  # 大了
        pa = [[p] + [-1] * m for p in parent]
        for i in range(m):
            for x in range(n):
                if (p := pa[x][i]) != -1:  # 必须要，不然 pa[-1][i]..
                    pa[x][i + 1] = pa[p][i]
        self.pa = pa

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if k >> i & 1:
                node = self.pa[node][i]
                if node < 0: break  # 必须要，不然 pa[-1][i] ...
        return node

    # 灵神
    # 另一种写法，不断去掉 k 的最低位的 1
    def getKthAncestor2(self, node: int, k: int) -> int:
        while k and node != -1:  # 也可以写成 ~node
            lb = k & -k
            node = self.pa[node][lb.bit_length() - 1]
            k ^= lb
        return node


# 我的”创新写法“
"""
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        pa = [[p] for p in parent]
        flag = True
        i = 0
        while flag:
            flag = False
            for x in range(n):
                if (p := pa[x][-1]) != -1:  # 必须要，不然 pa[-1][i]..
                    flag = True
                    pa[x].append(pa[p][i] if i < len(pa[p]) else -1)
            i += 1
        self.pa = pa

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if k >> i & 1:
                if i >= len(self.pa[node]): return -1
                node = self.pa[node][i]
                if node < 0: break  # 必须要，不然 pa[-1][i] ...
        return node
"""

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
# leetcode submit region end(Prohibit modification and deletion)

"""
["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
[[5,[-1,0,0,0,3]],[1,5],[3,2],[0,1],[3,1],[3,5]]
"""
