class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        maxprofit = 0
        for sell in range(buy + 1, len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            else: 
                maxprofit = max(maxprofit, prices[sell] - prices[buy])

        return maxprofit