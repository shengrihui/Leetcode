# 2251 花期内花的数目
import bisect
from collections import *
from itertools import *
from typing import *


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        n = max(max(people), max(e for _, e in flowers))
        diff = [0] * (n + 5)
        for s, e in flowers:
            diff[s] += 1
            diff[e + 1] -= 1
        a = list((accumulate(diff)))
        return [a[i] for i in people]


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        cnt = defaultdict(int)
        for s, e in flowers:
            cnt[s] += 1
            cnt[e + 1] -= 1
        a = sorted(cnt.items(), key=lambda x: x[0])
        indies = [i for i, _ in a]
        pre = [0] + list(accumulate([x for _, x in a])) + [0]
        return [pre[bisect.bisect_right(indies, p)] for p in people]

# leetcode submit region end(Prohibit modification and deletion)


# 给你一个下标从 0 开始的二维整数数组 flowers ，其中 flowers[i] = [starti, endi] 表示第 i 朵花的 花期 从 
# starti 到 endi （都 包含）。同时给你一个下标从 0 开始大小为 n 的整数数组 people ，people[i] 是第 i 个人来看花的时间。 
# 
#  请你返回一个大小为 n 的整数数组 answer ，其中 answer[i]是第 i 个人到达时在花期内花的 数目 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]
# 输出：[1,2,2,2]
# 解释：上图展示了每朵花的花期时间，和每个人的到达时间。
# 对每个人，我们返回他们到达时在花期内花的数目。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：flowers = [[1,10],[3,3]], people = [3,3,2]
# 输出：[2,2,1]
# 解释：上图展示了每朵花的花期时间，和每个人的到达时间。
# 对每个人，我们返回他们到达时在花期内花的数目。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= flowers.length <= 5 * 10⁴ 
#  flowers[i].length == 2 
#  1 <= starti <= endi <= 10⁹ 
#  1 <= people.length <= 5 * 10⁴ 
#  1 <= people[i] <= 10⁹ 
#  
# 
#  Related Topics 数组 哈希表 二分查找 有序集合 前缀和 排序 👍 60 👎 0
