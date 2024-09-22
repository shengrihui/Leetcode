# 第 416 场周赛 第 3 题
# 题目：100428. 统计重新排列后包含另一个字符串的子字符串数目 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-416/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/
# 题库：https://leetcode.cn/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i

from collections import Counter


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        cnt2 = Counter(word2)
        left = 0
        ans = 0
        cnt = Counter()
        for right, c in enumerate(word1):
            cnt[c] += 1
            while left <= right and all(v2 <= cnt[c2] for c2, v2 in cnt2.items()):
                cnt[word1[left]] -= 1
                left += 1
            print(left, right)
            ans += left
        return ans


s = Solution()
examples = [
    (dict(word1="bbbb", word2="b"), 10),
    (dict(word1="abcabc", word2="abc"), 10),
    (dict(word1="abcabc", word2="aaabc"), 0),
]
for e, a in examples:
    print(a, e)
    print(s.validSubstringCount(**e))
