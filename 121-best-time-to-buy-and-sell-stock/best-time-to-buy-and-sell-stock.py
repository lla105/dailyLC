class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyprice = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            price = prices[i]
            
            if buyprice > price:
                buyprice = price
            elif price - buyprice > profit:
                profit = price - buyprice

        return profit