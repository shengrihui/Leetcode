# 2003 每棵子树内缺失的最小基因值
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        ans = [1] * n  # 如果子树 i 没有1，ans[i]=1。需要修改的是 nums[i]=1 的子树，也就是 i和i的祖先节点
        if 1 not in nums:
            return ans

        # 建树
        g = [[] for _ in range(n)]  # g[i]：i的孩子节点
        for i in range(1, n):
            g[parents[i]].append(i)

        # 遍历子树x
        vis = set()

        def dfs(x: int) -> None:
            vis.add(nums[x])  # 将nums[x]放入集合中
            for son in g[x]:
                if nums[son] not in vis:  # nums[som]不在vis里，继续递归
                    dfs(son)

        mex = 2  # 最小缺失的基因值
        node = nums.index(1)  # noms[node]=1，从这开始
        while node >= 0:
            dfs(node)  # 遍历子树node
            while mex in vis:  # 枚举地找子树中缺失的最小值
                mex += 1
            ans[node] = mex
            node = parents[node]  # 去父节点（向上走）
        return ans

# leetcode submit region end(Prohibit modification and deletion)
