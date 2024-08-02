class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # from typing import List


        l = []
        for op in operations:
            if op == "C":
                if l:  
                    l.pop()
            elif op == "D":
                if l:  
                    l.append(2 * l[-1])
            elif op == "+":
                if len(l) >= 2:  
                    l.append(l[-1] + l[-2])
            else:
                l.append(int(op))
        return sum(l)
