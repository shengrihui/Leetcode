// 1470 重新排列数组
// https://leetcode.cn/problems/shuffle-the-array/


//leetcode submit region begin(Prohibit modification and deletion)


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shuffle(int* nums, int numsSize, int n, int* returnSize) {
    int* res = (int*)malloc(sizeof(int) * numsSize);
    *returnSize = numsSize;
    for (int i = 0; i < n; i++) {
        res[2 * i] = nums[i];
        res[2 * i + 1] = nums[i + n];
    }
    return res;
}
//leetcode submit region end(Prohibit modification and deletion)
