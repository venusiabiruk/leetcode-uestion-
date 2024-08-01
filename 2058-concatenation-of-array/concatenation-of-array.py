class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
       
        n = len(nums)
        output = []
        i = 0
        while i < 2:
            for j in range(n):
                output.append(nums[j])
            i +=1
        return output
            