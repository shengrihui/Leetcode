# 第 383 场周赛 第 4 题
# 题目：100203. 将单词恢复初始状态所需的最短时间 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-383/problems/minimum-time-to-revert-word-to-initial-state-ii/
# 题库：https://leetcode.cn/problems/minimum-time-to-revert-word-to-initial-state-ii


class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        z = [0] * n
        left, right = 0, 0
        for i in range(1, n):
            if i <= right:
                z[i] = min(right - i + 1, z[i - left])
            while i + z[i] < n and word[i + z[i]] == word[z[i]]:
                left, right = i, i + z[i]
                z[i] += 1
            if i % k == 0 and z[i] == n - i:  # i 在 xk 位，并且 z[i] = 后缀长度
                return i // k
        return (n - 1) // k + 1  # n/k 上取整


s = Solution()
examples = [
    (dict(word="abacaba", k=3), 2),
    (dict(word="abacaba", k=4), 1),
    (dict(word="abcbabcd", k=2), 4),
]
for e, a in examples:
    print(a, e)
    print(s.minimumTimeToInitialState(**e))
