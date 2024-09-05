class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        close = nums[0]
        for x in nums:
            if abs(close) > abs(x):
                close = x
        if close < 0 and abs(close) in nums:
            return abs(close)
        else:   
            return close

        
        





        