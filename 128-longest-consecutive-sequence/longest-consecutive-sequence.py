class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lo = 0 
        s = set(nums)
        for num in nums:
            if num-1 not in s:
                next_num = num+1
                le = 1
                while next_num in s:
                    le+=1
                    next_num += 1
                lo = max(lo,le)
        return lo




            

        