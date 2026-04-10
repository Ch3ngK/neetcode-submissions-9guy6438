class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length; 
        int buy = 0; 
        int max = 0;  

        for (int sell = 1; sell < n; sell++) {
            if (prices[buy] > prices[sell]) {
                buy = sell;
            } else {
                max = Math.max(max, prices[sell] - prices[buy]); 
            }
        }
        return max;
    }
}
