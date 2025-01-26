# 40 组合总和 II
# https://leetcode.cn/problems/combination-sum-ii/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i: int, rest: int) -> None:
            nonlocal t
            if rest == 0:  # 找到一种
                ans.append(t[:])
                return
            if i == len(cnt) or cnt[i][0] > rest:  # 没有数可以选了 or 待选的数都大了
                return

            dfs(i + 1, rest)  # 不选

            x, c = cnt[i]  # 当前要选的数，以及他一共有多少个
            most = min(rest // x, c)
            for j in range(1, most + 1):  # cnt[i][0] 一共有 cnt[i][1] 个
                t.append(x)  # 在组合中放 j 个 x
                dfs(i + 1, rest - j * x)
            t = t[:-most]  # 恢复现场

        cnt = sorted(Counter(candidates).items())
        ans = []
        t = []
        dfs(0, target)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
