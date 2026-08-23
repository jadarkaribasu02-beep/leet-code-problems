class Solution {
    public int maxProfit(int[] prices) {
        int mpr = Integer.MAX_VALUE;
        int  mp = 0;
        for(int i = 0; i<prices.length;i++){
            if(prices[i]<mpr){
                mpr = prices[i];
            }else if(prices[i] - mpr >mp){
                mp = prices[i] - mpr;
            }
        }
        return mp;
    }
}