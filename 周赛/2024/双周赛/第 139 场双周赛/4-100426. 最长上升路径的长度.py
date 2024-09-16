# 第 139 场双周赛 第 4 题
# 题目：100426. 最长上升路径的长度
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-139/problems/length-of-the-longest-increasing-path/
# 题库：https://leetcode.cn/problems/length-of-the-longest-increasing-path

from typing import List


def lengthOfLIS(nums):
    d = []
    for n in nums:
        if not d or n > d[-1]:
            d.append(n)
        else:
            l, r = 0, len(d) - 1
            loc = r
            while l <= r:
                mid = (l + r) // 2
                if d[mid] >= n:
                    loc = mid
                    r = mid - 1
                else:
                    l = mid + 1
            d[loc] = n
    return len(d)


class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        xx, yy = coordinates[k]
        # 第一要按 x 的顺序排
        # 然后要按 -y 的顺序排下标（y 的倒序）
        # 因为最终要构造一个 nums 求他的 LIS
        # 对于同一个 x 的不同 y 只能取一个，所以 y 要倒序排！！
        tmp1 = [(x, -y) for x, y in coordinates if x > xx and y > yy]
        tmp2 = [(x, -y) for x, y in coordinates if x < xx and y < yy]
        tmp1.sort()
        tmp2.sort()
        return lengthOfLIS([-y for x, y in tmp1]) + lengthOfLIS([-y for x, y in tmp2]) + 1


s = Solution()
examples = [
    (dict(coordinates=[[5, 0], [9, 3], [9, 8]], k=0), 2),
    (dict(coordinates=[[0, 3], [8, 5], [6, 8]], k=0), 2),
    (dict(coordinates=[[9, 8], [2, 1], [1, 0], [6, 0]], k=0), 3),
    (dict(coordinates=[[3, 1], [2, 2], [4, 1], [0, 0], [5, 3]], k=1), 3),
    (dict(coordinates=[[2, 1], [7, 0], [5, 6]], k=2), 2),
]
for e, a in examples:
    print(a, e)
    print(s.maxPathLength(**e))
