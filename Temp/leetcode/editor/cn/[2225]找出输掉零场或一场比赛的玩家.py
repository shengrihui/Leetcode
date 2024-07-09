# 2225 找出输掉零场或一场比赛的玩家
# https://leetcode.cn/problems/find-players-with-zero-or-one-losses/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        cnt = Counter()
        for w, l in matches:
            cnt[w] += 0
            cnt[l] += 1
        return [sorted(k for k, v in cnt.items() if v == t) for t in (0, 1)]
        # ans = [[], []]
        # for k, v in cnt.items():
        #     if v <= 1:
        #         ans[v].append(k)
        # ans[0].sort()
        # ans[1].sort()
        # return ans
# leetcode submit region end(Prohibit modification and deletion)
