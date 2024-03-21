class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyprice = prices[0]
        bestprofit = 0
        for i in range(1, len(prices)):
            buyprice = min(buyprice, prices[i])
            bestprofit = max(bestprofit, prices[i]-buyprice)
            # if prices[i] < buyprice:
            #     buyprice = prices[i]
            # elif bestprofit < prices[i] - buyprice:
            #     bestprofit = prices[i] - buyprice
        return bestprofit