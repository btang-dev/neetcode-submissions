class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l, r = 0, 1  # left pointer (buy) and right pointer (selling)
        while r < len(prices):
            # profitable ?
            if prices[l] < prices[r]: # as long as the buying price is less than the selling price
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit) # update the current maxP to the new profit
            else:
                l = r # shift all the way to the right to get the minimum
            r += 1 # iterate the right pointer after each calculation
        return maxP
