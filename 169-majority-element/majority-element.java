class Solution {
    public int majorityElement(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        int maj = 1, old =nums[0];

        for(int i = 1; i<n; i++){
            if(nums[i] == nums[i-1]){
                maj++;
            }else{
                maj = 1;
                old = nums[i];

            }if(maj>n/2){
                return old;
            }
        }
        return old;
        
    }
}