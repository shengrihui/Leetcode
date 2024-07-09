# 2368 受限条件下可到达节点的数目
# https://leetcode.cn/problems/reachable-nodes-with-restrictions/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        def dfs(x: int, fa: int) -> None:
            nonlocal ans
            ans += 1
            for y in g[x]:
                if y == fa or y in restr:
                    continue
                dfs(y, x)

        ans = 0
        restr = set(restricted)
        g = [[] for _ in range(len(edges)+1)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        dfs(0, -1)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
