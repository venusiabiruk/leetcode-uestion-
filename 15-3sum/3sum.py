class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans= []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i] >0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            lo,hi = i+1,n-1
            while lo<hi:
                sum = nums[i]+nums[lo]+nums[hi]
                if sum == 0:
                    ans.append([nums[i], nums[lo], nums[hi]])
                    lo+=1
                    hi -=1
                    while lo<hi and nums[lo] == nums[lo-1]:
                        lo+=1
                    while lo<hi and nums[hi] == nums[hi+1]:
                        hi-=1
                elif sum < 0:
                    lo +=1
                else:
                    hi-=1
        return ans






        








       
        # nums.sort()
        # triplets = []
        # n = len(nums)
        
        # for i in range(n - 2):
        #     # Skip duplicates for the first number
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
            
        #     left, right = i + 1, n - 1
        #     while left < right:
        #         total = nums[i] + nums[left] + nums[right]
        #         if total == 0:
        #             triplets.append([nums[i], nums[left], nums[right]])
        #             # Skip duplicates for the second number
        #             while left < right and nums[left] == nums[left + 1]:
        #                 left += 1
        #             # Skip duplicates for the third number
        #             while left < right and nums[right] == nums[right - 1]:
        #                 right -= 1
        #             # Move both pointers
        #             left += 1
        #             right -= 1
        #         elif total < 0:
        #             left += 1
        #         else:
        #             right -= 1
        
        # return triplets

        