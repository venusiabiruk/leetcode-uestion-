class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l , r = 0,len(nums)-1
        R = []
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                R.append(nums[l]**2)
                l+=1
            
            else:
                R.append(nums[r]**2)
                r-=1
        R.reverse()
        return R


        