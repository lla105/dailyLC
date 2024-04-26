class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyprice = inf
        bestprofit = 0

        for i in range(len(prices)):
            if prices[i] < buyprice:
                buyprice = prices[i]
            elif bestprofit < prices[i] - buyprice:
                bestprofit = prices[i] - buyprice
                
        return bestprofit
