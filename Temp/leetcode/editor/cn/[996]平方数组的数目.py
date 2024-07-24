# 996 平方数组的数目
# https://leetcode.cn/problems/number-of-squareful-arrays/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        d = defaultdict(list)
        cnt = Counter(nums)
        n = len(nums)
        for x in cnt:
            for y in cnt:
                t = sqrt(x + y)
                if t == int(t):
                    d[x].append(y)
            if not d[x]:
                return 0

        # 现在选的是 x ，还有 j 个数要选
        def dfs(x: int, j: int) -> int:
            cnt[x] -= 1
            if j == 0:
                res = 1
            else:
                res = 0
                for y in d[x]:
                    if cnt[y]:
                        res += dfs(y, j - 1)
            cnt[x] += 1
            return res

        ans = 0
        for x in cnt:
            ans += dfs(x, n - 1)
        return ans


# 记忆化搜索 + 状态压缩
"""
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        L = len(nums)
        targetState = (1 << L) - 1

        def check(a, b):
            c = sqrt(a + b)
            return c == int(c)

        @cache
        def dfs(pre, state):
            '''
            pre: 前一个数字
            state: nums的元素选取状态
            '''
            if state == targetState: return 1
            ans = 0
            s = set()
            # 枚举当前位置可用元素
            for i, n in enumerate(nums):
                # 对于元素n，若之前在当前位置已被使用过，那就跳过避免重复结果
                if state >> i & 1 == 0 and n not in s:
                    if pre is None or check(pre, n):
                        ans += dfs(n, state | (1 << i))
                        s.add(n)
            return ans
             
        return dfs(None, 0)
"""
# leetcode submit region end(Prohibit modification and deletion)
