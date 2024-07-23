# 第 135 场双周赛 第 3 题
# 题目：100365. 使差值相等的最少数组改动次数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-135/problems/minimum-array-changes-to-make-differences-equal/
# 题库：https://leetcode.cn/problems/minimum-array-changes-to-make-differences-equal

from collections import *
from itertools import *
from typing import List

# 方法一
"""
diff[d] = c : abs(nums[i] - nums[n-i-1]) = d 的个数有 c 个
按次数从大到小排序遍历 diff[d] = c

枚举到 diff[d] = c 的时候，也就是将每一对数的绝对差值变为 d（题目中的 x）
1. 当 d <= k // 2 时，
    若 nums[i] 和 nums[-i-1] 的绝对差值不是 d ，那不管它们是什么值，都可以只通过一次操作使得这对数的绝对差值变为 d
    总的操作次数为 n//2 - c （有 c 对数的绝对差值是 d 了不用变，其他的都操作一次）
    而又因为是按 c 降序遍历的，后续不会有更好的答案了
        假设后面有 diff[dd] = cc <= c ，无论 dd 的大小，要想将其他数对的绝对差值改为 dd ，至少要操作 n // 2 - cc 次，
        而 n // 2 - cc >= n // 2 - c，所以不会哟更好的答案了。
2. 当 n // 2 - c >= ans 的时候，不会有更好的答案了，理由如上。
3. 暴力统计操作次数
    现在数对为 (x,y)，想要让他们的绝对差值变为 d
    想象在数轴上以 x 或 y 为圆心 d 为半径画圆，
    如果圆与 [0,k] 有交点，那么可以只操作一次（修改一个数）使得两数的绝对差值变为 d，
    否则就要操作两次（两个数都要修改）。
    当然如果他们的绝对差值本来就是 d 就不用动啦~
"""


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        diff = Counter()
        for i in range(n // 2):
            diff[abs(nums[i] - nums[-1 - i])] += 1
        diff = sorted([(c, d) for d, c in diff.items()], reverse=True)
        ans = n
        for c, d in diff:
            if d <= k // 2:
                ans = min(ans, n // 2 - c)
                break
            if n // 2 - c >= ans:
                break
            t = 0
            for i in range(n // 2):
                x, y = nums[i], nums[-i - 1]
                if abs(x - y) == d:
                    continue
                if x + d <= k or x >= d or y + d <= k or y >= d:
                    t += 1
                else:
                    t += 2
            if t < ans:
                ans = t
        return ans


# 方法二
"""
枚举 X ，那将所有数对的绝对差值改为 X 需要操作多少次呢？
对于数对 (p,q) (q>=p)，
若 q-p=d，不需要修改
若 max(q,k-p) >= X ，改一次
若 max(q,k-p) < X ，改两次

用 cnt 记录 q-p 的个数，cnt1 记录 max(q,k-p) 的个数
那么 X 要修改的次数 = n//2 - cnt[X] + cnt1[0] + ...+ cnt1[X-1]
"""


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = [0] * (k + 1)
        cnt1 = [0] * (k + 1)
        for i in range(n // 2):
            p, q = nums[i], nums[-1 - i]
            if q < p:
                p, q = q, p
            cnt[q - p] += 1
            cnt1[max(q, k - p)] += 1
        s = 0
        ans = n
        for c, c1 in zip(cnt, cnt1):
            ans = min(ans, n // 2 - c + s)
            s += c1
        return ans


# 方法三
"""
数对 (p,q) 
x = abs(p-q) 
mx = max(p,k-q,q,k-p)
将 x 修改成 ：
1. [0,x-1]  1 次
2. x        0 次
3. [x+1,mx] 1 次
4. [mx+1,k] 2 次

差分数组 d[X] 的前缀和 pre[X] 表示
将 x 修改成 X 的操作次数
"""


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        d = [0] * (k + 2)
        for i in range(len(nums) // 2):
            q, p = nums[i], nums[-i - 1]
            x = abs(p - q)
            mx = max(p, k - p, q, k - q)
            d[0] += 1
            d[x] -= 1
            d[x + 1] += 1
            d[mx + 1] += 1  # -1 +2 = +1
        return min(accumulate(d))


s = Solution()
examples = [
    (dict(nums=[4, 2, 4, 0, 3, 3, 0, 0, 0, 1, 4, 1], k=4), 2),
    (dict(nums=[1, 0, 1, 2, 4, 3], k=4), 2),
    (dict(nums=[0, 1, 2, 3, 3, 6, 5, 4], k=6), 2),
    (dict(nums=[2, 66, 37, 2, 47, 28, 28, 18, 51, 2, 68, 56, 34, 63, 1, 57, 5, 53, 46, 36, 11, 50, 50, 2, 21, 9, 17, 30,
                43, 33, 26, 13, 69, 23, 66, 52, 49, 40, 39, 49, 66, 56], k=70), 20),
]
for e, a in examples:
    print(a, e)
    print(s.minChanges(**e))
