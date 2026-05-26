class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):

            sell = prices[i]

            _p = sell - buy
            if max_profit < _p:
                max_profit = _p
            if prices[i] < buy:
                buy = prices[i]
        
        return max_profit