class Solution {
public:
    int thirdMax(vector<int>& arr) {
        int n = arr.size();

        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] < arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }

        int count = 1;

        for (int i = 1; i < n; i++) {
            if (arr[i] != arr[i - 1]) {
                count++;

                if (count == 3) {
                    return arr[i];
                }
            }
        }

        return arr[0];
    }
};