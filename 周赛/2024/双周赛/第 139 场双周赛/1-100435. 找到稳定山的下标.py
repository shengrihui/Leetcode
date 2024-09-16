# 第 139 场双周赛 第 1 题
# 题目：100435. 找到稳定山的下标
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-139/problems/find-indices-of-stable-mountains/
# 题库：https://leetcode.cn/problems/find-indices-of-stable-mountains

from typing import List


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        return [i for i in range(1, len(height)) if height[i - 1] > threshold]


s = Solution()
examples = [
    (dict(height=[1, 2, 3, 4, 5], threshold=2), [3, 4]),
    (dict(height=[10, 1, 10, 1, 10], threshold=3), [1, 3]),
    (dict(height=[10, 1, 10, 1, 10], threshold=10), []),
]
for e, a in examples:
    print(a, e)
    print(s.stableMountains(**e))
