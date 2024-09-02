// 1512 好数对的数目
// https://leetcode.cn/problems/number-of-good-pairs/


//leetcode submit region begin(Prohibit modification and deletion)
int numIdenticalPairs(int* nums, int numsSize) {
    int* cnt = (int*)malloc(sizeof(int) * 101);
    memset(cnt, 0, sizeof(int) * 101);
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        ans += cnt[nums[i]]++;
    }
    free(cnt);
    return ans;
}
//leetcode submit region end(Prohibit modification and deletion)
