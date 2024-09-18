class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = "balloon"
        c = defaultdict(int)
        for i in text:
            if i in b:
                c[i] += 1
        if any(i not in c for i in b):
            return 0
        else:
            return min(c["b"],c["a"],c["l"]//2,c["o"]//2,c["n"])
                

    


        


            

        
        