# 2007 从双倍数组中还原原数组
# https://leetcode.cn/problems/find-original-array-from-doubled-array/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n == 0 or n % 2 == 1:  # 本身空或者是奇数个
            return []
        changed.sort(reverse=True)
        cnt = Counter()
        ans = []
        for x in changed:
            if cnt[x] > 0:  # 当前值是之前数的一半
                cnt[x] -= 1
                continue
            # 当前值是倍数
            if x % 2 == 1:
                return []
            y = x // 2
            cnt[y] += 1
            ans.append(y)
        # 存在着有些数的一半不在 change 里
        if sum(cnt.values()) > 0:
            return []
        return ans

# leetcode submit region end(Prohibit modification and deletion)
