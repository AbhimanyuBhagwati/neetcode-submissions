class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit =0
        buy = float("inf")

        for i in prices:
            buy = min(i, buy)
            _pr = i - buy
            max_profit = max(_pr, max_profit)
        
        return max_profit