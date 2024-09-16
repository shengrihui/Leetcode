# 第 139 场双周赛 第 3 题
# 题目：100429. 求出数组中最大序列值
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-139/problems/find-the-maximum-sequence-value-of-array/
# 题库：https://leetcode.cn/problems/find-the-maximum-sequence-value-of-array

from functools import reduce
from operator import or_
from typing import List


# https://leetcode.cn/problems/find-the-maximum-sequence-value-of-array/solutions/2917604/qian-hou-zhui-fen-jie-er-wei-0-1-bei-bao-8icz

class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # from operator import or_
        mx = reduce(or_, nums)  # 计算 nums 里的所有数的 or 和

        # 后缀
        # suf[i] 在 nums[i:] 中选 k 个数所有结果，
        # 一共有 n - k + 1 个数的后面（包括）有 k 个数（[n-k+1:] 有 k 个数）
        suf = [None] * n  # (n - k + 1)
        # 在后缀遍历到 nums[i] 的时候，f[j] 表示 nums[i:] 中选 j 个数可能所有 or 结果
        # 因为要算 f[k] 所以 k + 1
        f = [set() for _ in range(k + 1)]
        f[0].add(0)  # 初始啥也不选放个 0
        for i in range(n - 1, k - 1, -1):  # 倒着遍历 [k,n-1]
            v = nums[i]
            for j in range(k - 1, -1, -1):
                # 从 f[j] 中选出 x 或上 v 加到 f[j+1] 里
                f[j + 1].update(x | v for x in f[j])
            suf[i] = f[k].copy()

        # 前缀
        # 同时计算答案
        ans = 0
        f = [set() for _ in range(k + 1)]
        f[0].add(0)
        for i, v in enumerate(nums[:-k]):  # 到倒数第 k 个的前一个
            for j in range(k - 1, -1, -1):
                f[j + 1].update(x | v for x in f[j])
            # 更新答案
            if f[k]:
                ans = max(ans, max(y ^ x for y in f[k] for x in suf[i + 1]))
                if ans == mx:
                    break
        return ans


s = Solution()
examples = [
    (dict(nums=[2, 6, 7], k=1), 5),
    (dict(nums=[4, 2, 5, 6, 7], k=2), 2),
]
for e, a in examples:
    print(a, e)
    print(s.maxValue(**e))
