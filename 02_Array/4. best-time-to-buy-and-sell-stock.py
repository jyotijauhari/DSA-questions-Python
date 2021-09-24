class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]

        for i in range(1, len(prices)):
            temp = prices[i] - minPrice
            maxProfit = max(maxProfit, temp)
            minPrice = min(minPrice, prices[i])
        return maxProfit