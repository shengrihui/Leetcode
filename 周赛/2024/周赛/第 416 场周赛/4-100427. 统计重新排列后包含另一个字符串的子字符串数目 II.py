# 第 416 场周赛 第 4 题
# 题目：100427. 统计重新排列后包含另一个字符串的子字符串数目 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-416/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/
# 题库：https://leetcod e.cn/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii

from collections import Counter


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            return 0
        cnt = Counter(word2)
        left = ans = 0
        # less: cnt[c] <= 0 的数量
        # cnt[c] <= 0 表示 c 在窗口中的数量比在 word2 中的多了
        less = len(cnt)
        for c in word1:
            cnt[c] -= 1
            if cnt[c] == 0:  # cnt[c] 减小到了 0
                less -= 1
            while less == 0:  # 移动 left 缩小窗口
                if cnt[word1[left]] == 0:
                    less += 1
                cnt[word1[left]] += 1
                left += 1
            ans += left
        return ans


s = Solution()
examples = [
    (dict(word1="dcbdcdccb", word2="cdd"), 18),
    (dict(word1="bbbb", word2="b"), 10),
    (dict(word1="bcca", word2="abc"), 1),
    (dict(word1="abcabc", word2="abc"), 10),
    (dict(word1="abcabc", word2="aaabc"), 0),
]
for e, a in examples:
    print(a, e)
    print(s.validSubstringCount(**e))
