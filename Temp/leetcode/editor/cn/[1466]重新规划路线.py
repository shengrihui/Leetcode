# 1466 重新规划路线


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        in_, out = [[] for _ in range(n)], [[] for _ in range(n)]
        for a, b in connections:  # a 到 b
            in_[b].append(a)
            out[a].append(b)

        def dfs(i: int, fa: int) -> None:
            nonlocal ans
            ans += len(out[i]) - (fa in out[i])
            for son in chain(in_[i], out[i]):
                if son != fa:
                    dfs(son, i)
            # ans += len(out[i])
            # for son in in_[i]:
            #     if son != fa:
            #         dfs(son, i)
            # for son in out[i]:
            #     if son != fa:
            #         dfs(son, i)
            #     else:
            #         ans -= 1

        ans = 0
        dfs(0, -1)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
