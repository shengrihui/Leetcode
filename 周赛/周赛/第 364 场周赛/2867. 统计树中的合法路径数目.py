from typing import List

# 题目：# 2867. 统计树中的合法路径数目
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-364/problems/count-valid-paths-in-a-tree/
# 题库：https://leetcode.cn/problems/count-valid-paths-in-a-tree/description/

MX = 10 ** 5
# is_prime = [True] * (MX + 1)
# is_prime[1] = is_prime[0] = False
# for i in range(2, isqrt(MX) + 1):
#     if is_prime[i]:
#         for j in range(i * i, MX + 1):
#             if j % i == 0:
#                 is_prime[j] = False
#
# print([x for x, is_p in enumerate(is_prime) if is_p])
is_prime = [True] * (MX + 1)
is_prime[1] = False
primes = []
for i in range(2, MX + 1):
    if is_prime[i]:
        primes.append(i)
    for min_prime in primes:
        if i * min_prime > MX:
            break
        is_prime[i * min_prime] = False
        if i % min_prime == 0:
            break


# print(primes)


class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(x: int, fa: int) -> None:
            if is_prime[x]:  # 遇到质数退出
                return
            nodes.append(x)
            for y in g[x]:
                if y != fa:
                    dfs(y, x)

        ans = 0
        size = [0] * (n + 1)
        for x in range(1, n + 1):
            if not is_prime[x]:  # 如果x不是质数，跳过
                continue
            s = 0  # 包含 x 的合法路径的数量
            # x有好多分支，也就是好多连通块，遍历这些分支，计算每个连通块的大小
            for y in g[x]:
                nodes = []  # y所在这个连通块包含的节点
                if size[y] == 0:  # 这个连通块还没有计算过
                    dfs(y, x)
                for z in nodes:  # 连通块的里每一个节点的 size 都是 len(nodes)
                    size[z] = len(nodes)
                ans += s * size[y]  # s是已经累积到现在的合法路径数量，size[y]是当前连通块的的大小
                # 为什么 size[y]!=len(nodes) 呢?因为 size[y] 可能已经计算过了，不进行 dfs，那 len(nodes)=0
                s += size[y]
            ans += s
        return ans


s = Solution()
examples = [
    (dict(n=5, edges=[[1, 2], [1, 3], [2, 4], [2, 5]]), 4),
    (dict(n=6, edges=[[1, 2], [1, 3], [2, 4], [3, 5], [3, 6]]), 6),
]
for e, a in examples:
    print(a, e)
    print(s.countPaths(**e))
