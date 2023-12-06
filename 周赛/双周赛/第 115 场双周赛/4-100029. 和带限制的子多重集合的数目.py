from typing import List
from collections import *
from itertools import *

# 题目：100029. 和带限制的子多重集合的数目
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-115/problems/count-of-sub-multisets-with-bounded-sum/
# 题库：https://leetcode.cn/problems/count-of-sub-multisets-with-bounded-sum/

# 多重背包（朴素）
"""
class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        MOD = 10 ** 9 + 7
        cnt = Counter(nums)
        n = len(cnt)
        dp = [[0] * (r + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i, (x, c) in enumerate(cnt.items()):
            for j in range(r + 1):
                for k in range(c + 1):
                    if j - k * x >= 0:
                        dp[i + 1][j] = (dp[i + 1][j] + dp[i][j - k * x]) % MOD
                    else:
                        break
        return sum(dp[-1][l:r + 1]) % MOD
"""

# 优化1第一步：式子变形
"""
假设 cnt[x] = 3
dp[i][j - x] = dp[i - 1][j - x] + dp[i - 1][j - 2 * x] + dp[i - 1][j - 3 * x] + dp[i - 1][j - 4 * x]
所以：
dp[i - 1][j - x] + dp[i - 1][j - 2 * x] + dp[i - 1][j - 3 * x] = dp[i][j - x] - dp[i - 1][j - 4 * x]
dp[i][j] = dp[i - 1][j] + (dp[i - 1][j - x] + dp[i - 1][j - 2 * x] + dp[i - 1][j - 3 * x])
dp[i][j] = dp[i - 1][j] + dp[i][j - x] - dp[i - 1][j - 4 * x]
一般地，
dp[i][j] = dp[i - 1][j] + dp[i][j - x] - dp[i - 1][j - (cnt[x] + 1) * x]
如果 j - (cnt[x] + 1) * x < 0
那就当这一部分是0，dp[i][j] = dp[i - 1][j] + dp[i][j - x]
当然，j也是要比x大于等于的
为什么直接当成0就可以，dp[i][j] = dp[i - 1][j] + dp[i][j - x] 成立呢？
因为这个递推式中的dp[i][j - x]已经包含了dp[i - 1][j - x]、dp[i-1][j - 2 * x] 等计算dp[i][j]所需要的那些值了

因此，这回必须要特殊考虑 cnt[0]了
因为如果存在 cnt[0]，在后面的遍历每一个数的时候，假设第一次就是0吧，
dp[i - 1][j]和dp[i - 1][j - (cnt[x] + 1) * x]是一样的，会出错哦

"""
"""
class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        MOD = 10 ** 9 + 7
        cnt = Counter(nums)
        n = len(cnt) - (0 in cnt)
        dp = [[0] * (r + 1) for _ in range(n + 1)]
        dp[0][0] = cnt[0] + 1
        del cnt[0]
        for i, (x, c) in enumerate(cnt.items()):
            for j in range(r + 1):
                dp[i + 1][j] = (dp[i][j] +
                                (dp[i + 1][j - x] if j >= x else 0) -
                                (dp[i][j - (c + 1) * x] if j - (c + 1) * x >= 0 else 0)) 
        return sum(dp[-1][l:r + 1]) % MOD
"""

# 优化1第二步：滚动数组（空间）+j的范围
"""
改不成原地一行的，因为，状态转移方程里既有当前行的也有上一行的

j的方位是从x到当前所有数加起来的和与r的最小值+1
"""
"""
class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        MOD = 10 ** 9 + 7
        cnt = Counter(nums)
        dp = [[0] * (r + 1) for _ in range(2)]
        dp[1][0] = cnt[0] + 1
        del cnt[0]
        cur_i = 1
        s = 0
        for i, (x, c) in enumerate(cnt.items()):
            cur_i = i % 2
            s = min(r, s + c * x) + 1
            pre_i = 1 - cur_i
            for j in range(r + 1):
                dp[cur_i][j] = dp[pre_i][j] % MOD if cur_i else dp[pre_i][j]
            for j in range(x, s):
                dp[cur_i][j] = (dp[pre_i][j] +
                                (dp[cur_i][j - x] if j >= x else 0) -
                                (dp[pre_i][j - (c + 1) * x] if j - (c + 1) * x >= 0 else 0)) % MOD
        return sum(dp[cur_i][l:r + 1]) % MOD
"""

# 优化方法2：同余前缀和优化
"""
（打脸前面）
对上面的方法改成一维数组
dp[cur_i][j] = (dp[pre_i][j] +
                (dp[cur_i][j - x] if j >= x else 0) -
                (dp[pre_i][j - (c + 1) * x] if j - (c + 1) * x >= 0 else 0)) % MOD
其中，dp[cur_i][j - x]是更新后的，而另外两个是更新前的
所以，可以遍历两遍，
第一遍 -dp[pre_i][j - (c + 1) * x]
    而且这一遍得从后往前！！！！
    因为dp[pre_i][j - (c + 1) * x]得要是之前的之前的之前的没有修改的
第二遍 dp[cur_i][j - x]
进一步地，
j的范围亦可以调整，使下标取值合适
"""


class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        MOD = 10 ** 9 + 7
        cnt = Counter(nums)
        dp = [0] * (r + 1)
        dp[0] = cnt[0] + 1
        del cnt[0]
        s = 0
        for x, c in cnt.items():
            s = min(r, s + c * x)
            for j in range(s, (c + 1) * x - 1, -1):
                dp[j] -= dp[j - (c + 1) * x]
            for j in range(x, s + 1):
                dp[j] = (dp[j] + dp[j - x]) % MOD
        return sum(dp[l:]) % MOD


s = Solution()
examples = [
    # (dict(nums=[1, 2, 2, 3], l=6, r=6), 1),
    (dict(nums=[2, 1, 4, 2, 7], l=1, r=5), 7),
    # (dict(nums=[1, 2, 1, 3, 5, 2], l=3, r=5), 9),
    # (dict(nums=[0, 0, 1, 2, 3], l=2, r=3), 9),
]
for e, a in examples:
    print(a, e)
    print(s.countSubMultisets(**e))
