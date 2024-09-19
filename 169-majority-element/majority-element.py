class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = defaultdict(int)
        m = len(nums)/2
        for i in nums:
            if i in c:
                c[i] += 1
            else:
                c[i] = 1
            if c[i] >= m:
                return i

    

    
        


            


        