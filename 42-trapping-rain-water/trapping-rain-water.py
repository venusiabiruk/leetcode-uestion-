class Solution:
    def trap(self, height: List[int]) -> int:
        lwall = 0
        rwall = 0
        n = len(height)
        maxl = [0] *n
        maxr = [0] *n
        for i in range(n):
            j = -i-1
            maxl[i] = lwall
            maxr[j] = rwall
            lwall = max(lwall,height[i])
            rwall = max(rwall,height[j])

        sum = 0
        for i in range(n):
            pot = min(maxl[i],maxr[i])
            sum+= max(0,pot-height[i])
        return sum 






        