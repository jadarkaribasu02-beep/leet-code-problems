class Solution {
    public int thirdMax(int[] arr) {

        int n = arr.length;

        
        for (int i = 0; i < n - 1; i++) {

            int max = i;

            for (int j = i + 1; j < n; j++) {
                if (arr[j] > arr[max]) {
                    max = j;
                }
            }

           
            int temp = arr[i];
            arr[i] = arr[max];
            arr[max] = temp;
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
}