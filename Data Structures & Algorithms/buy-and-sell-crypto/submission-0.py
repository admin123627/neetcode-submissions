class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        for i, a in enumerate(prices):
            max_next = max(prices[i:])
            maximum = max(maximum, max_next - a)
        return maximum