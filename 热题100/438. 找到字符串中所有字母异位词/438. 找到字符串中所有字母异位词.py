# https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def findAnagrams(self, s: str, p: str):  # -> List[int]:
        f = lambda i: ord(s[i]) - ord('a')
        d = [-1 if chr(i + ord('a')) not in p else 0 for i in range(26)]
        ans = []
        for c in p:
            d[ord(c) - ord('a')] += 1
        l, r = 0, 0
        n, m = len(s), len(p)
        while l < n and r <= n:
            # print(l, r, d)
            if r == n and r - l != m:
                break
            if r - l == m:
                ans.append(l)
                d[f(l)] += 1
                l = l + 1
                # r = r + 1
                # print(l, r, d)
                # return ans
            else:
                if d[f(r)] > 0:
                    d[f(r)] -= 1
                    r += 1
                else:
                    # r+=1
                    # while l < r:
                    if d[f(l)] != -1:
                        d[f(l)] += 1
                        l += 1
                    if d[f(r)] == -1 and l == r:
                        l += 1
                        r += 1

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
