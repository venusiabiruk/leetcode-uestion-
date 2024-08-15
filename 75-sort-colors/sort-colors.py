class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, mid, r = 0, 0, len(nums) - 1
        
        while mid <= r:
            if nums[mid] == 0:
                # Swap nums[low] and nums[mid], increment both low and mid
                nums[l], nums[mid] = nums[mid], nums[l]
                l += 1
                mid += 1
            elif nums[mid] == 1:
                # Move mid pointer if nums[mid] is 1
                mid += 1
            else:
                # Swap nums[mid] and nums[high], decrement high
                nums[r], nums[mid] = nums[mid], nums[r]
                r -= 1
