# 825 适龄的朋友
# https://leetcode.cn/problems/friends-of-appropriate-ages/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# https://leetcode.cn/problems/friends-of-appropriate-ages/solutions/1174365/gua-ling-de-peng-you-by-leetcode-solutio-v7yk
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        ans = right = left = 0
        for age in ages:
            # 0.5 * ages[x] + 7 < ages[y] <= ages[x]
            # ages[x] >= 14 但当 age[x] = 14 的时候，0.5 * ages[x] + 7 = 14
            # 即 14 < ages[y] <= 14 ，不存在这样的 ages[y]
            if age < 15:
                continue
            # [left, right] 也就是 x 在 right 可以向 [left, right] 中的 y 发请求
            while ages[left] <= (age * 0.5 + 7):
                left += 1
            while right + 1 < len(ages) and ages[right + 1] <= age:
                right += 1
            ans += right - left
        return ans
# leetcode submit region end(Prohibit modification and deletion)
