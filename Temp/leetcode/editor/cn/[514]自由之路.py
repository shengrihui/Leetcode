# 514 自由之路
# https://leetcode.cn/problems/freedom-trail/


# leetcode submit region begin(Prohibit modification and deletion)
# 记忆化搜索 + 二分
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @cache
        def dfs(j: int, i: int) -> int:  # 当前 12:00 是 ring[i]，要拼写的是 key[j]
            if j == m:  # 拼写完了
                return 0
            if key[j] == ring[i]:  # 不需要旋转，拼写下一个
                return dfs(j + 1, i)
            # ring[d[key[j]][pos]] 和 ring[d[key[j]][pos-1]] 都是当前要拼写的字母
            pos = bisect.bisect_left(d[key[j]], i) % len(d[key[j]])  # pos 可能会是 len(d[key[j]) 所以要 %
            idx1, idx2 = d[key[j]][pos], d[key[j]][pos - 1]
            return min(dfs(j + 1, idx1) + (idx1 - i) % n, dfs(j + 1, idx2) + (i - idx2) % n)

        n, m = len(ring), len(key)
        d = defaultdict(list)
        for i, c in enumerate(ring):
            d[c].append(i)
        return m + dfs(0, 0)


# BFS
"""
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n, m = len(ring), len(key)
        q = deque()
        q.append((0, 0))
        vis = [[False] * (m + 1) for _ in range(n)]
        step = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if j == m:  # 已经拼写完 key
                    return step
                if ring[i] == key[j]:  # 12:00 方向已经是当前要拼写的字母，j 后移
                    if not vis[i][j + 1]:
                        vis[i][j + 1] = True
                        q.append((i, j + 1))
                    continue  # 不需要旋转了
                for ni in ((i - 1) % n, (i + 1) % n):  # 当前 12:00 不是要拼写的字母，继续旋转
                    if not vis[ni][j]:
                        vis[ni][j] = True
                        q.append((ni, j))
            step += 1  # 旋转一个位置 / 已经是当前要拼写的字母“按下”的操作
"""
# leetcode submit region end(Prohibit modification and deletion)
