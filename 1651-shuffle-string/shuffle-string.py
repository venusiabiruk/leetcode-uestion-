class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        r= [None]*len(s)
        for i in range(len(s)):
            fp = indices[i]
            char = s[i]
            r[fp] = char
        A = ''.join(r)
        return A

      



