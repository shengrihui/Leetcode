from typing import List


# 题目：# 8050. 统计一个字符串的 k 子序列美丽值最大的数目
# 题目链接： https://leetcode.cn/contest/biweekly-contest-112/problems/count-k-subsequences-of-a-string-with-maximum-beauty/
class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        if k > 26:
            return 0
        mod = 10 ** 9 + 7
        count = [0] * 26
        ans = 1
        for ch in s:
            count[ord(ch) - 97] += 1

        count.sort(key=lambda x: -x)
        print(count)
        k_counts = count[k - 1]
        k_counts_nums = 0
        select = 0
        for b in count:
            if b > k_counts:
                select += 1
                ans = ans * b % mod
            elif b == k_counts:
                k_counts_nums += 1
            else:
                break
            if select == k:
                return ans % mod

        # 计算Ck_counts_nums取需要
        # print(ans)
        rest = k - select
        up = 1
        down = 1
        for i in range(rest):
            up *= k_counts_nums - i
            down *= i + 1
        # print(c_count)
        # print(rest, up, down, k_counts_nums, (up // down))
        ans = ans * (k_counts ** rest) * (up // down) % mod
        return ans % mod


s = Solution()
examples = [
    (dict(s="bcca", k=2), 4),
    (dict(s="abbcd", k=4), 2),
    (dict(s="aabbaabbaabb", k=2), 60),
    (dict(s="dd", k=2), 0),
    (dict(s="elex", k=4), 0),
]
for e, a in examples:
    print(e, a)
    print(s.countKSubsequencesWithMaxBeauty(**e))
