class Solution {
public:
    int search(vector<int>& arr, int target) {
        int n = arr.size() -1;
        int low = 0;
        int high = n;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1;
    }
};