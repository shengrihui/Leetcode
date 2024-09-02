// 2708 一个小组的最大实力值
// https://leetcode.cn/problems/maximum-strength-of-a-group/


//leetcode submit region begin(Prohibit modification and deletion)
#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))
long long maxStrength(int* nums, int numsSize) {
    long long mn = nums[0], mx = nums[0];
    for (int i = 1; i < numsSize; i++) {
        int x = nums[i];
        long long a = mn * x;
        long long b = mx * x;
        mx = max(max(x, mx), max(a, b));
        mn = min(min(x, mn), min(a, b));
    }
    return mx;
}
//leetcode submit region end(Prohibit modification and deletion)
