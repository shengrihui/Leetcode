from typing import List


# https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        count = [0] * 26
        for i in range(p_len):
            count[ord(s[i]) - 97] += 1
            count[ord(p[i]) - 97] -= 1

        differ = [c != 0 for c in count].count(True)

        if differ == 0:
            ans.append(0)
        # count记录的是窗口（p长度）内字母的数量
        # s里多，是正数，p里多是负数，一样多是0
        for i in range(s_len - p_len):
            # print(count)
            # print(differ)
            if count[ord(s[i]) - 97] == 1:  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从不同变得相同
                differ -= 1
            elif count[ord(s[i]) - 97] == 0:  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从相同变得不同
                differ += 1
            count[ord(s[i]) - 97] -= 1
            # print(count)
            # print(differ)
            if count[ord(s[i + p_len]) - 97] == -1:  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从不同变得相同
                differ -= 1
            elif count[ord(s[i + p_len]) - 97] == 0:  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从相同变得不同
                differ += 1
            count[ord(s[i + p_len]) - 97] += 1
            # print(count)
            # print(differ)
            # print()
            if differ == 0:  # 这个时候相同的是 i+1 开始
                ans.append(i + 1)

        return ans


s = Solution()
examples = [
    dict(s="cbaebabacd", p="abc"),
    dict(s="abacbabc", p="abc"),
    dict(s="baa", p="aa"),
    dict(s="abab", p="ab")
]
for e in examples:
    print(e)
    print(s.findAnagrams(**e))
