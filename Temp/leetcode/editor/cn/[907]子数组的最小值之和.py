# 907 子数组的最小值之和
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        # arr[i]=x 可以作为最小值的范围 (left,right)
        # left：左边小于 x 的地方，arr[left] < arr[i]
        # right：右边小于等于 x 的位置，arr[right] >= arr[i]
        # 等于的情况主要是为了避免重复
        # 比如 [1,2,3,2,4] arr[1]的是(0,5),arr[3]的也是(0,5)，在下面计算贡献就会重复
        # 所以将 right 的定义修改了
        # 贡献计算：
        # 可以作为子数组左端点：left+1,left+2,...,i
        # 可以作为子数组右端点：i,...,right-2,right-1
        # 子数组数量：(i-left)*(right-i)
        # 贡献：x*(i-left)*(right-i)
        # 寻找 left和right：单调栈
        # left：从左往右，入栈钱，将比 x 大的弹出，等于也弹出，剩下栈顶那个就是 arr[i] 的 left，然后入栈
        # right：从右往左，入栈钱，将比 x 大的弹出，等于不弹出，剩下栈顶那个就是 arr[i] 的 right，然后入栈

        # 三次遍历
        """
        st = []
        left = [-1] * n
        for i, x in enumerate(arr):
            while st and x <= arr[st[-1]]:
                st.pop()
            if st: left[i] = st[-1]
            st.append(i)
        st = []
        right = [n] * n
        for i in range(n - 1, -1, -1):
            while st and arr[i] < arr[st[-1]]:
                st.pop()
            if st: right[i] = st[-1]
            st.append(i)
            
        for i, x, l, r in zip(range(n), arr, left, right):
            ans += x * (i - l) * (r - i)
        """

        # 两次遍历
        # 在遍历 left 的时候，弹出 st[-1] 对应的 arr[st[-1]] 大于等于 arr[i]
        # 也就是：i 正好是 st[-1] 的 right
        """
        st = []
        left = [-1] * n
        right = [n] * n
        for i, x in enumerate(arr):
            while st and x <= arr[st[-1]]:
                right[st.pop()] = i
            if st: left[i] = st[-1]
            st.append(i)

        for i, x, l, r in zip(range(n), arr, left, right):
            ans += x * (i - l) * (r - i)
        """

        # 一次遍历
        # 栈顶的下一个元素 st[-2] 是栈顶的 left
        # 而它的 right 是在它因为 arr[st[-1]] >= arr[i] 而弹出的时候确定为 i
        # 又为了最后所有那些栈里的值都能在出栈的时候计算到 ans 里，可以在 arr 最后面加上 -1
        # 又因为为了要 st[-2]（弹出栈顶之后的st[-1]） ，所以 st 初始为 [-1] ，作为 st[1] 的 left
        arr.append(-1)
        st = [-1]
        for right, x in enumerate(arr):
            # while len(st) > 1 and arr[st[-1]] >= x:
            while arr[st[-1]] > x:  # arr[-1]=-1 一定不满足，一开始一定不进入循环
                i = st.pop()
                ans += arr[i] * (i - st[-1]) * (right - i)
            st.append(right)
        return ans % (10 ** 9 + 7)

# leetcode submit region end(Prohibit modification and deletion)
