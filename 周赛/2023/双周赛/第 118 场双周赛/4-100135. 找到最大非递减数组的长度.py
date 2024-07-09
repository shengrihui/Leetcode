# 题目：100135. 找到最大非递减数组的长度
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-118/problems/find-maximum-non-decreasing-array-length/
# 题库：https://leetcode.cn/problems/find-maximum-non-decreasing-array-length
from collections import deque
from itertools import accumulate
from typing import List

"""
f[i] 表示 nums[0] 到 nums[i] 合并后的最大数组长度

last[i] 表示在 f[i] 尽可能大的前提下，分组后的最后一组的和的最小值
last[i] 越小，越有利于后面获得更大的 f

如果 nums[j+1] + nums[j+2] + ... + nums[i] >= last[j] ,
那么 f[i] 可以从 f[j] 转移过来 f[i] = f[j] + 1
要找满足条件的最大 j

答案 f[n-1] 

在代码中，下标从 1 开始
f[i+1] 表示 nums[0] 到 nums[i] 合并后的最大数组长
last[i+1] 表示 nums[0] 到 nums[i 表示在 f[i+1] 尽可能大的前提下，分组后的最后一组的和的最小值 
就是和前缀和数组一样在最前面加了个 0

前缀和数组 s[i+1] 表示 nums[0] 加到 nums[i]
nums[j+1] + nums[j+2] + ... + nums[i]  >= last[j+1]
-> s[i+1] - s[j+1] >= last[j+1]
那都有 +1 就不要了
-> s[i] - s[j] >= last[j]
-> s[i] >= s[j] + last[j]

接下来就是找满足 s[i] >= s[j] + last[j] 的最大的 j 作为转移来源

考虑 k < j,有 f[k] <= f[j] （因为 f 是非递减的）
且 s[k] + last[k] 和 s[j] + last[j] 都 <= s[i] ，都可以转移到 i
那么就选择从大的 j 转移
单调队列
队列中保存的是下标，单调递增的

1. 转移之前，去掉队首
保证队首的是最大的满足 s[j] + last[j] <= s[i] 的 j
所以要比较队的第二个元素和 s[i]

2. 转移
    f[i] = f[q[0]] + 1
    last[i] = s[i] - s[q[0]]

3. 转移之后，去掉队尾的
    在队尾可能会存在 s[j] + last[j] 比现在的 s[i] + last[i] 还要大的，去掉
    如果不去掉，之后就会容易有较小的 j 满足 s[j] + last[j] <= s[i] 了
"""


class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        f = [0] * (n + 1)
        last = [0] * (n + 1)
        q = deque([0])
        for i in range(1, n + 1):
            while len(q) > 1 and s[q[1]] + last[q[1]] <= s[i]:
                q.popleft()
            f[i] = f[q[0]] + 1
            last[i] = s[i] - s[q[0]]
            while q and s[q[-1]] + last[q[-1]] >= s[i] + last[i]:
                q.pop()
            q.append(i)
        return f[n]


s = Solution()
examples = [
    (dict(nums=[5, 2, 2]), 1),
    (dict(nums=[1, 2, 3, 4]), 4),
    (dict(nums=[4, 3, 2, 6]), 3),
]
for e, a in examples:
    print(a, e)
    print(s.findMaximumLength(**e))
