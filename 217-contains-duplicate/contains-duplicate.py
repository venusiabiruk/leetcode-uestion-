class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = set()
        for i in nums:
            if i in h:
                return True
            else:
                h.add(i)
        return False
                
        