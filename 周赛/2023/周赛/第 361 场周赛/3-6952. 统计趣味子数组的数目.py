from collections import defaultdict
from typing import List

# 题目：# 6952. 统计趣味子数组的数目
# 题目链接：https://leetcode.cn/problems/count-of-interesting-subarrays/description/
# 竞赛：https://leetcode.cn/contest/weekly-contest-361/problems/count-of-interesting-subarrays

"""
首先可以将原数组中的 nums[i] % m == k 的数看成是 1

那 cnt 的计算可以由前缀和数组计算：
cnt = s[R+1] - s[L]

问题变成了有多少 L,R 使 cnt % m == k
(s[R+1] - s[L]) % m == k
或 (s[R+1] - s[L] + m) % m == k （python 可以不用考虑）
转换：
s[R+1] % m - s[L] % m == k
也就是 s[l] % m + k == s[r] % m, l!=r 两数之和
     遍历 s ，ans+=cnt[x-k] cnt[x]+=1
"""


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        # s = [0] * (n + 1)  # 前缀和数组
        # for i, x in enumerate(nums):
        #     s[i + 1] = s[i] + (x % modulo == k)
        # cnt = defaultdict(int)
        # ans = 0
        # for x in s:
        #     ans += cnt[(x - k) % modulo]
        #     cnt[x % modulo] += 1
        # return ans

        # 不用 s 数组
        ans = s = 0
        cnt = defaultdict(int)
        cnt[0] = 1  # 前缀和前面补的 0
        for x in nums:
            s += x % modulo == k
            ans += cnt[(s - k) % modulo]
            cnt[s % modulo] += 1
        return ans


s = Solution()
examples = [
    (dict(nums=[3, 2, 4], modulo=2, k=1), 3),
    (dict(nums=[3, 1, 9, 6], modulo=3, k=0), 2),
    (dict(nums=[2, 2, 5], modulo=3, k=2), 2),
]
for e, a in examples:
    print(a, e)
    print(s.countInterestingSubarrays(**e))
