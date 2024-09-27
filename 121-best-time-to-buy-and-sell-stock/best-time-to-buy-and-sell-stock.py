class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        n = len(prices)

        for r in range(1, n):
            if prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r  # Update l to r when a lower price is found

        return max_profit


       
        # maxp = 0 
        # cheepp = prices[0]
        # for i in range(1,len(prices)):
        #     if prices[i] < cheepp:
        #         cheepp = prices[i]
        #     current = prices[i] - cheepp
        #     maxp = max(maxp,current)
        # return maxp



            






        