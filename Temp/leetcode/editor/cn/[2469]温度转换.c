// 2469 温度转换
// https://leetcode.cn/problems/convert-the-temperature/

// leetcode submit region begin(Prohibit modification and deletion)
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double *convertTemperature(double celsius, int *returnSize)
{
    double *res = (double *)malloc(sizeof(double) * 2);
    res[0] = celsius + 273.15;
    res[1] = celsius * 1.80 + 32.00;
    *returnSize = 2;
    return res;
}
// leetcode submit region end(Prohibit modification and deletion)
