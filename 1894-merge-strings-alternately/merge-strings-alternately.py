class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A,B = len(word1), len(word2)
        a,b = 0,0
        list1 = []
        word = 1
        while a < A and b < B:
            if word == 1:
                list1.append(word1[a])
                a+=1
                word = 2
            if word == 2:
                list1.append(word2[b])
                b +=1
                word = 1
        while a < A:
            list1.append(word1[a])
            a += 1
        while b <B:
            list1.append(word2[b])
            b += 1
        return''.join(list1)
       











        