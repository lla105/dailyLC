class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # decisions: 
        # - buy or sell. to sell, need to buy first
        # - either we buy or don't buy
        # - buy, sell
        # - if cur price < prev price, buy price = cur price
        # - if sell price > buy price, update profit.
        profit = 0
        buy_price = float('inf')
        for i in range(len(prices)):
            if prices[i] < buy_price :
                buy_price = prices[i]
            else:
                profit = max(profit, abs(buy_price - prices[i] ))
        return profit