# 题目：100163. 统计强大整数的数目
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-121/problems/count-the-number-of-powerful-integers/
# 题库：https://leetcode.cn/problems/count-the-number-of-powerful-integers

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        s_int = int(s)
        if s_int >= finish:  # s 本身就比 finish 大，那在 [start,finish] 里就没有强数了，但如果 s==finish，还能有一个
            return int(s_int == finish)

        def int_len(x: int) -> int:
            # 计算 整数 x 的长度
            ans = 0
            while x:
                ans += 1
                x //= 10
            return ans

        s_len = len(s)
        sk = 10 ** s_len  # 经常用到

        low = max(s_int, start)
        if s_int < start % sk:
            # 向前进位，后面全减少为0
            low += sk - start % sk
        # 每一位都要比 limit 小或等于，哪一位大了往前进位，再将这一位及其往后的变为 0
        for k in range(s_len, int_len(low)):
            kk = pow(10, k)
            r = low // kk % 10  # 当前这一位的值
            if r > limit:
                low += (10 - r) * kk  # 当前位往前进 1 # low += kk * 10
                low = low // kk * kk  # 将后面全部变成 0
        low //= sk

        upper = finish - (10 ** s_len if s_int > finish % sk else 0)
        # 每一位都要比 limit 小或等于，哪一位大了就把这一位及其往后都变成 limit
        flag = False
        for k in range(int_len(upper), s_len - 1, -1):
            kk = pow(10, k)
            r = upper // kk % 10  # 当前这一位的值
            if flag or r > limit:  # 当前这一位变为 limit
                upper -= (r - limit) * kk
                flag = True
        upper //= sk

        def f(x: int) -> int:
            li = limit + 1
            # 将 li进制 数转为十进制数
            ans = 0
            k = 1
            while x:
                ans += x % 10 * k
                k *= li
                x //= 10
            return ans

        return f(upper) - f(low) + 1


s = Solution()
examples = [
    (dict(start=1, finish=6000, limit=4, s="124"), 5),
    (dict(start=15, finish=215, limit=6, s="10"), 2),
    (dict(start=1000, finish=2000, limit=4, s="3000"), 0),
    (dict(start=141, finish=148, limit=9, s="9"), 0),
    (dict(start=20, finish=1159, limit=5, s="20"), 8),
    (dict(start=1829505, finish=1255574165, limit=7, s="11223"), 5470),
    (dict(start=1114, finish=1864854501, limit=7, s="26"), 4194295),
    (dict(start=697662853, finish=11109609599885, limit=6, s="5"), 16135677999),
    (dict(start=71617670092, finish=478940209902614, limit=8, s="10"), 1380457214216),
]
for e, a in examples:
    # print(e)
    print(s.numberOfPowerfulInt(**e) == a)
