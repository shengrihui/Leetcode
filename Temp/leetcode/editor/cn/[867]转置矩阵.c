// 867 转置矩阵
// https://leetcode.cn/problems/transpose-matrix/


//leetcode submit region begin(Prohibit modification and deletion)
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** transpose(int** matrix, int matrixSize, int* matrixColSize, int* returnSize, int** returnColumnSizes) {
    int** res = (int**)malloc(sizeof(int*) * (*matrixColSize));
    *returnSize = *matrixColSize;
    *returnColumnSizes = (int*)malloc(sizeof(int) * (*matrixColSize));

    for (int i = 0; i < *matrixColSize; i++) {
        res[i] = (int*)malloc(sizeof(int) * matrixSize);
        (*returnColumnSizes)[i] = matrixSize;  // 为每一列设置其大小

        for (int j = 0; j < matrixSize; j++) {
            res[i][j] = matrix[j][i];  // 进行转置操作
        }
    }
    return res;
}
//leetcode submit region end(Prohibit modification and deletion)
