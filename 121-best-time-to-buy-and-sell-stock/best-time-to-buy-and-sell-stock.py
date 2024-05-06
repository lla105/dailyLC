class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyprice = float('inf')
        answer = float('-inf')
        for price in prices:

            if price < buyprice:
                buyprice = price
            profit = price - buyprice
            answer = max(answer, profit)
        if answer>0:
            return answer
        else:
            return 0
