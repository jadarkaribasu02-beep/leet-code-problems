class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;

        int sum = (n*(n+1))/2;
        int asum =0 ;
        

        for(int i =0;i<n;i++){
            asum = asum + nums[i];
        }
        int miss_number= sum - asum;
        return miss_number;


    }
}