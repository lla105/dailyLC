class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = float('inf')
        maxprofit = 0
        maxprofit = float('-inf')
        for i in range(len(prices)):
            if prices[i] < cheapest:
                cheapest = prices[i]
            else:
                maxprofit = max(maxprofit , prices[i] - cheapest )

        if maxprofit<0:
            return 0
        else:
            return maxprofit