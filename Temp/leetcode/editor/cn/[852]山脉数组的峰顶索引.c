// 852 山脉数组的峰顶索引
// https://leetcode.cn/problems/peak-index-in-a-mountain-array/


//leetcode submit region begin(Prohibit modification and deletion)
int peakIndexInMountainArray(int* arr, int arrSize) {
    int left = 1, right = arrSize-1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (arr[mid] >= arr[mid - 1] && arr[mid] >= arr[mid + 1])
            return mid;
        else if (arr[mid] >= arr[mid - 1] && arr[mid] <= arr[mid + 1])
            left = mid + 1;
        else if (arr[mid] <= arr[mid - 1] && arr[mid] >= arr[mid + 1])
            right = mid - 1;
    }
    return -1;
}
//leetcode submit region end(Prohibit modification and deletion)
