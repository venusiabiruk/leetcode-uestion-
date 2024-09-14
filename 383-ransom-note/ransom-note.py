class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = {}
        for i in magazine:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        for i in ransomNote:
            if i not in map:
                return False
            elif map[i] == 1 :
                del map[i]
            else:
                map[i] -= 1
        return True



        