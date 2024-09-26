class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        lo = 0
        se = set()
        for r in range(len(s)):
            while s[r] in se:
                se.remove(s[l])
                l+=1
            w = (r-l)+1
            lo = max(lo,w)
            se.add(s[r])
        return lo



        