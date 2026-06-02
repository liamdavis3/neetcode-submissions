class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 0
        high = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                money = prices[right] - prices[left]
                if money > high:
                    high = money
            else:
                left = right
            right += 1
        return high
            

