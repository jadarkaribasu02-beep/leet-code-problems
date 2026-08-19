class Solution {
    public void merge(int[] k1, int m, int[] k2, int n) {

        int idx = m + n - 1;
        int i = m - 1;
        int j = n - 1;

        while (i >= 0 && j >= 0) {

            if (k1[i] >= k2[j]) {
                k1[idx] = k1[i];
                i--;
            } else {
                k1[idx] = k2[j];
                j--;
            }

            idx--;
        }

        // Copy remaining elements of k2
        while (j >= 0) {
            k1[idx] = k2[j];
            idx--;
            j--;
        }
    }
}