class Solution {
public:
    int majorityElement(vector<int>& arr) {
        int n = arr.size();
        int majority_count = 0;
        int ans = 0;

        for (int i = 0; i < n; i++) {
            int counter = 1;

            for (int j = i + 1; j < n; j++) {
                if (arr[i] == arr[j]) {
                    counter++;
                }
            }

            if (counter > majority_count) {
                majority_count = counter;
                ans = arr[i];
            }

            if (majority_count > n / 2) {
                return ans;
            }
        }

        return ans;
    }
};