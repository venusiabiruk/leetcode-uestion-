class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        l,r = 1,n
        while l <= r:
            mid = (l+r)//2
            c = (mid/2)*(mid +1)
            if c > n:
                r = mid -1
            else:
                l = mid +1
                res = max(mid,res)
        return res




        