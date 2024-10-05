class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pc = 0
        nc = 0
        for num in nums:
            if num > 0:
                pc +=1
            elif num <0:
                nc += 1
        return max(pc,nc)




        