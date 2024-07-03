# 第 125 场双周赛 第 4 题
# 题目：100210. 最大节点价值之和
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-125/problems/find-the-maximum-sum-of-node-values/
# 题库：https://leetcode.cn/problems/find-the-maximum-sum-of-node-values

from math import inf
from typing import List

"""
1. 可以转换成对 nums 任意两个值，与树无关了
对于一条 x 到 y 的路径，只有两端的 x 和 y 只异或了一次，中间的节点都异或了两次

2. 一共会有偶数个数异或了
如果 x 和 y 两个数中，
都没有异或，那操作之后异或的数的数量 +2
都异或过，那操作之后异或的数的数量 -2
一个异或过另一个没有异或，那操作之后异或的数的数量 +1-1=0 不变

3.问题变成
从 nums 中选偶数个数异或后最大值是多少？

状态定义：
f[i][0] 前 i 个数中选 偶数 个数异或后最大价值
f[i][1] 前 i 个数中选 奇数 个数异或后最大价值
状态转移：
f[i+1][0] = max(f[i][0] + x, f[i][1] + (x^k)) 选择异或或者不异或
F[i+1][0] = max(f[i][1] + x, f[i][0] + (x^k))
初始值：
f[0][0] = 0, f[0][1] = -inf
答案：
f[n][0]
空间优化：
可以只用 f0 和 f1 两个变量
"""


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        f0, f1 = 0, -inf
        for x in nums:
            f0, f1 = max(f0 + x, f1 + (x ^ k)), max(f1 + x, f0 + (x ^ k))
        return f0


# 树形 DP
# https://leetcode.cn/problems/find-the-maximum-sum-of-node-values/solutions/2664309/liang-chong-fang-fa-shu-xing-dp-xian-xin-lh6b
"""
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        g = [[] for _ in nums]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(x: int, fa: int) -> (int, int):
            f0, f1 = 0, -inf  # f[x][0] 和 f[x][1]
            for y in g[x]:
                if y != fa:
                    r0, r1 = dfs(y, x)
                    f0, f1 = max(f0 + r0, f1 + r1), max(f1 + r0, f0 + r1)
            return max(f0 + nums[x], f1 + (nums[x] ^ k)), max(f1 + nums[x], f0 + (nums[x] ^ k))
        return dfs(0, -1)[0]
"""
s = Solution()
examples = [
    (dict(nums=[1, 2, 1], k=3, edges=[[0, 1], [0, 2]]), 6),
    (dict(nums=[2, 3], k=7, edges=[[0, 1]]), 9),
    (dict(nums=[7, 7, 7, 7, 7, 7], k=3, edges=[[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]), 42),
]
for e, a in examples:
    print(a, e)
    print(s.maximumValueSum(**e))
