# 996 正方形数组的数目
# https://leetcode.cn/problems/number-of-squareful-arrays/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        d = defaultdict(list)
        cnt=Counter(nums)
        se = set(nums)
        n = len(nums)
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if i == j: continue
                t = sqrt(x + y)
                if t == int(t):
                    d[x].append(y)
            if not d[x]:
                return 0
        ans = set()

        def dfs(path: List[int], x: int, fa: int) -> None:
            if len(path) == n:
                nonlocal ans
                ans.add(tuple(path))
                return
            for y in d[x]:
                if  cnt[y]>Counter(path)[y]:
                    dfs(path + [y], y, x)

        for x in se:
            dfs([x], x, -1)
        return len(ans)

# leetcode submit region end(Prohibit modification and deletion)
