# 第 408 场周赛 第 3 题
# 题目：100348. 统计 1 显著的字符串的数量
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-408/problems/count-the-number-of-substrings-with-dominant-ones/
# 题库：https://leetcode.cn/problems/count-the-number-of-substrings-with-dominant-ones


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        a = [i for i, c in enumerate(s) if c == "0"]
        tot1 = n - len(a)  # 1 的个数
        a.append(n)  # 最后全是 1 的情况，加一个哨兵
        ans = i = 0  # 内层循环中遍历 0 的位置在 a 中的起点
        for left, c in enumerate(s):
            for k in range(i, len(a) - 1):
                cnt0 = k - i + 1  # 0 的个数
                if cnt0 * cnt0 > tot1:  # [left:] 的 1 的个数都比现在枚举的 0 的个数小了，那就 break
                    break
                p, q = a[k], a[k + 1]  # 两个相邻的 0 的位置
                cnt1 = p - left + 1 - cnt0
                if cnt1 >= cnt0 * cnt0:
                    # p,p+1,...q-1 都可以作为子串的右端点
                    ans += q - p
                else:
                    # 1 的数量不够，需要 cnt0*cnt0 - cnt1 个
                    ans += max(q - (p + cnt0 * cnt0 - cnt1), 0)
            if c == "0":
                i += 1
            else:
                tot1 -= 1
                ans += a[i] - left  # 没有 0 的情况
        return ans


s = Solution()
examples = [
    (dict(s="00011"), 5),
    (dict(s="101101"), 16),
]
for e, a in examples:
    print(a, e)
    print(s.numberOfSubstrings(**e))
