# 2916 子数组不同元素数目的平方和 II
from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
"""
前面参考[2262]字符串总引力
nums = [1,2,2,3,1]
从左往右遍历整个数组
以当前这个数字为开头到当前遍历到的数字为结尾的这个子串有多少个不同的数字^2     ans=平方和
a
1           ans1 
a   b       
2^2 1^2         ans2 
a   b   b
2^2 1^2 1^2       ans3 
a   b   b   c
3^2 2^2 2^2 1^2     ans4 
a   b   b   c   a
3^2 3^2 3^2 2^2 1^2   ans5 
规律（总结）
ans5 - ans4 = 3^2-2^2 + 3^2-2^2 + 2^2-1^2 + 1^2-0^2
            = 2*2+1 + 2*2+1 + 2*1+1 + 2*0+1
            = 2(2+2+1)+4
==========================================================================================
设第 i 个数字上一次出现的位置是 j
nums[0..i-1] 的不同计数 x[0]
nums[1..i-1] 的不同计数 x[1]
nums[j..i-1] 的不同计数 x[j]
nums[i-1..i-1] 的不同计数 x[i-1]
x[i]=0
加入 nums[i] 之后，x[0] 到 x[j] 不变， x[j+1] 到 x[i] 都加1
所有不同计数的平方和的增量 = (x[j+1]+1)^2-x[j+1]^2 + (x[j+2]+1)^2-x[j+2]^2 + .. + (x[i]+1)^2-x[i]^2
                      = 2*x[j+1]+1 + 2*x[j+2]+1 + ... + 2*x[i]+1
                      = 2sum(x[j+1 .. i]) + (i-j)
==========================================================================================
1.每一次操作都是对一个区间内的值+1 （x[j+1] 到 x[i] 都加1）
2.每一次查询都是返回一个区间的和   （sum(x[j+1 .. i])）
因此，用线段树。
“每一次”就是往后遍历，新加入一个数。
操作和查询的是同一个区间。
要维护的 sum[o] 初始全为0，不需要build了
每一次 查询/操作 ：
1. 返回 sum(x[j+1 .. i]
2. 更新 x[j+1 ... i]
    =>
3. 维护 sum(x[j+1 .. i]
"""


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        sum = [0] * (4 * n)
        todo = [0] * (4 * n)  # 对区间内的每一个值（x[i]）要增加多少

        def do(o: int, l: int, r: int, add: int) -> None:
            """
            add来自于：
            1. query_and_add 递归结束时，对 x[l...r] 都+1
            2. 从父节点传递过来的 todo[o]，对 x[l...r] 都+add
            表示 x[l...r] 加上多少
            =》 sum[o] += 区间长度 * add

            todo[o]表示
            节点 o 这个区间累加了多少，是一个标记/记录的作用，主要是向下传递的时候会用到
            """
            sum[o] += (r - l + 1) * add
            todo[o] += add

        def query_and_add(o: int, l: int, r: int, L: int, R: int) -> int:
            """
            l,r：当前节点代表的区间
            L,R：要查询/更新的区间
            返回：要查询的区间的 sum(x[l...r])
            当 [l,r] ⊂ [L,R]，返回 sum(x[l...r]) 即 sum[o]，并结束递归
            因为 sum(x[l...r]) 会由好多“特殊区间”组成，要递归左右孩子，所以，res 要 +=
            """
            if L <= l and r <= R:
                res = sum[o]
                do(o, l, r, 1)  # x[l...r]都要加1
                return res
            m = (l + r) // 2
            if todo[o]:  # 向下传递
                do(o * 2, l, m, todo[o])
                do(o * 2 + 1, m + 1, r, todo[o])
                todo[o] = 0
            res = 0
            if m >= L:
                res += query_and_add(o * 2, l, m, L, R)
            if m < R:  # m+1<=R
                res += query_and_add(o * 2 + 1, m + 1, r, L, R)
            # 维护 sum[o]
            sum[o] = sum[o * 2] + sum[o * 2 + 1]
            return res

        last = {}
        ans = s = 0
        for i, x in enumerate(nums, 1):  # 起始索引设为1
            j = last.get(x, 0)
            # 要查询的范围是[j+1,i]
            delta = query_and_add(1, 1, n, j + 1, i) * 2 + i - j  # 平方和的增量
            s += delta  # 到x的平方和
            ans = (ans + s) % MOD
            last[x] = i
        return ans
# leetcode submit region end(Prohibit modification and deletion)
