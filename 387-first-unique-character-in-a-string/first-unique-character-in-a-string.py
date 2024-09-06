class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = 0
        f = {}
        for i in s:
            if i  in f:
                f[i] += 1
            else:
                f[i] = 1
        for index, i in enumerate(s):
            if f[i] == 1:
                return index
            
        return -1
        