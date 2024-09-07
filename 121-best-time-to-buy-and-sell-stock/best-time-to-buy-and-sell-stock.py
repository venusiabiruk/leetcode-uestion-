class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0 
        cheepp = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < cheepp:
                cheepp = prices[i]
            current = prices[i] - cheepp
            maxp = max(maxp,current)
        return maxp



            






        