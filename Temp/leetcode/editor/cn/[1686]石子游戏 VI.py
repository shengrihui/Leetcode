# 1686 石子游戏 VI
# https://leetcode.cn/problems/stone-game-vi/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        # v = sorted([(a + b, i) for i, (a, b) in enumerate(zip(aliceValues, bobValues))], reverse=True)
        # a, b = sum(aliceValues[i] for va, i in v[::2]), sum(bobValues[i] for va, i in v[1::2])
        # return 1 if a > b else (0 if a == b else -1)
        v = sorted([a + b for a, b in zip(aliceValues, bobValues)], reverse=True)
        ans = sum(v[::2]) - sum(bobValues)  # alice 和 bob 最后的价值差
        return 1 if ans > 0 else (0 if ans == 0 else -1)
# leetcode submit region end(Prohibit modification and deletion)
