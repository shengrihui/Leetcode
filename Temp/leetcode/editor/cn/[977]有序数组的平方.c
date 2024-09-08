// 977 有序数组的平方
// https://leetcode.cn/problems/squares-of-a-sorted-array/

//leetcode submit region begin(Prohibit modification and deletion)
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortedSquares(int* nums, int numsSize, int* returnSize) {
    int* ans = (int*)malloc(sizeof(int) * numsSize);
    *returnSize = numsSize;
    int i = 0, j = numsSize - 1;
    for (int p = *returnSize - 1; p >= 0; p--) {
        int x = nums[i], y = nums[j];
        if (-x > y) {
            ans[p] = x * x;
            i++;
        } else {
            ans[p] = y * y;
            j--;
        }
    }
    return ans;
}
//leetcode submit region end(Prohibit modification and deletion)
