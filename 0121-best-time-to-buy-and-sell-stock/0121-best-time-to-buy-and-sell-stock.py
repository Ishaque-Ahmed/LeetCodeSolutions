class Solution(object):
    def maxProfit(self, prices):
        leftPointer = 0
        rightPointer = 1
        maxProfit = 0

        while rightPointer != len(prices):
            if prices[leftPointer] < prices[rightPointer]:
                profit = prices[rightPointer] - prices[leftPointer]
                maxProfit = max(maxProfit, profit)
            else: 
                leftPointer = rightPointer
            
            rightPointer += 1
        
        return maxProfit

        