class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j = 0,1
        max_profit = 0
        while j<len(prices):
            k = prices[j] - prices[i]
            if prices[j]>prices[i]:
                max_profit=max(max_profit,k)
                j+=1
            else:
                i = j
                j+=1
        return max_profit
        
