class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestprice = max(prices)
        bestprofit = -1

        for i in range(len(prices)):
            p = prices[i]
            if bestprice > p:
                bestprice = p
            else:
                bestprofit = max(bestprofit, p-bestprice)

        if bestprofit<0:
            return 0
        else:
            return bestprofit