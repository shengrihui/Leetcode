# 题目：100156. 转换字符串的最小成本 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-377/problems/minimum-cost-to-convert-string-i/
# 题库：https://leetcode.cn/problems/minimum-cost-to-convert-string-i
from math import *
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        def o(c: str) -> int:
            return ord(c) - 97

        mp = [[inf] * 26 for _ in range(26)]
        for org, ch, c in zip(original, changed, cost):
            mp[o(org)][o(ch)] = min(c, mp[o(org)][o(ch)])

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    mp[i][j] = min(mp[i][k] + mp[k][j], mp[i][j])
        ans = 0
        for s, t in zip(source, target):
            if s == t: continue
            if mp[o(s)][o(t)] == inf:
                return -1
            ans += mp[o(s)][o(t)]
        return ans


# 这个速度快
"""
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        nodes = set(original + changed)
        dist = {node: {node2: inf for node2 in nodes} for node in nodes}

        for node in nodes:
            dist[node][node] = 0
        
        for s, d, c in zip(original, changed, cost):
            dist[s][d] = min(dist[s][d], c)
…            score = dist.get(src, {}).get(des, inf)
            if score == inf:
                return -1

            total_cost += score

        return total_cost
"""
s = Solution()
examples = [
    (dict(source="abcd", target="acbe", original=["a", "b", "c", "c", "e", "d"], changed=["b", "c", "b", "e", "b", "e"],
          cost=[2, 5, 5, 1, 2, 20]), 28),
    (dict(source="aaaa", target="bbbb", original=["a", "c"], changed=["c", "b"], cost=[1, 2]), 12),
    (dict(source="abcd", target="abce", original=["a"], changed=["e"], cost=[10000]), -1),
]
for e, a in examples:
    print(a, e)
    print(s.minimumCost(**e))
