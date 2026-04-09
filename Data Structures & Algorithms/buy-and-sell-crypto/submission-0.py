class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = float("inf")
        max_profit = 0
        for i in range(len(prices)):
            profit = prices[i] - min_value
            min_value = min(prices[i], min_value)

            max_profit = max(profit, max_profit)
        return max_profit


        