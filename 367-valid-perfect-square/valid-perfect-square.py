class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 0,num
        while l <= r:
            mid = (l+r)//2
            s = mid * mid 
            if s == num:
                return True
            elif s > num:
                r = mid -1
            else:
                l = mid + 1
        return False 
        


        