# 2028 找出缺失的观测数据
# https://leetcode.cn/problems/find-missing-observations/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        r = mean * (len(rolls) + n) - sum(rolls)
        if r < n or r > n * 6:
            return []
        ans = [r // n] * n
        for i in range(r % n):
            ans[i] += 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
