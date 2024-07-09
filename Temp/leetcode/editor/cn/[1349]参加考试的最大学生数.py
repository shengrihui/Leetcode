# 1349 参加考试的最大学生数
# https://leetcode.cn/problems/maximum-students-taking-exam/

# leetcode submit region begin(Prohibit modification and deletion)
"""
# 二进制的表示：
1：这座位不是坏的，可以坐 / 这个座位因为后排会作弊而不能被选择
0：这座位坏的，不能被选择 / 这个座位不会被作弊

# 一些计算与二进制表示
记这一排的二进制表示为j，s 是 j 的子集
上一排的二进制表示为t

## 
这一排是否有相邻的 1： s>>1 & s （或 s<<1 & s）
结果为 0 表示没有相邻的 1
如果有两个相邻的二进制位是 1，在左边的右移1位之后按位与原来的结果一定不为0

## 
lowbit：s & -s  (只有最右边的 1 那一位是 1)
最后一位1和它左边那一位：lowbit<<1 | lowbit = lowbit * 3 （只有那两位是 1 其余位为 0）

## 
将最后一位1和它左边那一位置为 0 ：
先做出只有那两位是0其余位是1 ~(lowbit * 3)
再与原来的按位与 s & ~(lowbit * 3)

##
这一排一个可选的方案 s（没有相邻的1）
对应上一排的座位影响是： s<<1 | s>>1 （这时候 1 表示因为作弊不能选）
那么上一排的座位集合是：
先将“影响”取反：~(s<<1 | s>>1)  这样0表示因为作弊不能选的位置
再与原来的 t 取交集： t & ~(s<<1 | s>>1) 原来位置是好的但因为作弊也不能被选所以要 &

## 初始化
s = 0
for j,c in enumerate(s):
    s += (c == ".") << j # 如果从左往右第 j 位是 .，那么二进制从右往左第 j 位是 1

# 第 0 排最多可以坐多少学生
贪心地递归地取最右边可以选的位置，然后把它和它相邻的置为 0

"""


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        a = [sum((c == ".") << j for j, c in enumerate(s)) for s in seats]

        @cache
        def dfs(i: int, j: int) -> int:
            if i == 0:
                lb = j & -j
                # 将最右边的 1 和它相邻的二进制置为 0，然后递归计算
                # +1：lowbit选择坐了学生
                return dfs(0, j & ~(lb * 3)) + 1 if j else 0
            res = dfs(i - 1, a[i - 1])  # 第 i 排不坐学生，直接看 i-1 排
            s = j  # s 是 j 的子集
            while s:
                if s >> 1 & s == 0:
                    # 当前这一子集没有相邻的1，也就是这一排可以的一个方案
                    # 这时候 1 表示安排学生坐，那么学生人数=1的个数
                    t = a[i - 1] & ~(s << 1 | s >> 1)  # i-1 排现在的状态
                    res = max(res, s.bit_count() + dfs(i - 1, t))
                s = (s - 1) & j
            return res

        return dfs(len(seats) - 1, a[-1])
# leetcode submit region end(Prohibit modification and deletion)
