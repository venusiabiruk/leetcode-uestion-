class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lm = 1
        rm = 1
        n = len(nums)
        arrl = [0] *n
        arrr = [0] *n
        for i in range(n):
            j = -i -1
            arrl[i] = lm
            arrr[j] = rm
            lm *= nums[i]
            rm *= nums[j]
        return[l*r for l,r in zip(arrl,arrr)]
        

        
        

        