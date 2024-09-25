// 2535 数组元素和与数字和的绝对差
// https://leetcode.cn/problems/difference-between-element-sum-and-digit-sum-of-an-array/


//leetcode submit region begin(Prohibit modification and deletion)
int differenceOfSum(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        ans += x;
        while (x) {
            ans -= x % 10;
            x /= 10;
        }
    }
    return ans;
}
//leetcode submit region end(Prohibit modification and deletion)
