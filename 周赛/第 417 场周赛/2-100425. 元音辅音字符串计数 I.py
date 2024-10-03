# 第 417 场周赛 第 2 题
# 题目：100425. 元音辅音字符串计数 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-417/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/
# 题库：https://leetcode.cn/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        d = {c: i for i, c in enumerate("aeiou")}
        cnt = [0] * 5
        fy = 0
        ans = left = right = 0
        n = len(word)
        while right < n:
            rc = word[right]
            if rc in d:
                cnt[d[rc]] += 1
            else:
                fy += 1
            tleft = left
            tcnt = cnt.copy()
            tfy = fy
            while min(tcnt) >= 1 and tfy >= k:
                lc = word[tleft]
                if lc in d:
                    tcnt[d[lc]] -= 1
                    if tcnt[d[lc]] == 0:
                        break
                    if tfy == k:
                        print(1, word[tleft:right + 1])
                    ans += tfy == k
                    tleft += 1
                else:
                    if tfy > k:
                        cnt = tcnt.copy()
                        fy = tfy
                        left = tleft
                    if tfy == k:
                        print(2, word[tleft:right + 1])
                        ans += 1
                    tfy -= 1
            right += 1
        return ans


s = Solution()
examples = [
    (dict(word="iqeaouqi", k=2), 3),
    (dict(word="aeioqq", k=1), 0),
    (dict(word="aeiou", k=0), 1),
    (dict(word="ieaouqqieaouqq", k=1), 3),
]
for e, a in examples:
    print(a, e)
    print(s.countOfSubstrings(**e))
