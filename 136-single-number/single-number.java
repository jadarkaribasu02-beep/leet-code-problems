class Solution {
    public int singleNumber(int[] nums) {
        int sngl = 0;
        for (int x : nums) {
            sngl = sngl ^ x;
        }
        return sngl;

    }
}