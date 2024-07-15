class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highestprice = prices[-1]
        maxprofit = 0
        for i in range(len(prices)-1, -1, -1):
            # print(i,'). ', highestprice, prices[i])
            if prices[i] >= highestprice:
                highestprice = prices[i]
            else:
                maxprofit = max(maxprofit , highestprice-prices[i])
            # print(' >>>> ', highestprice)
        return maxprofit
