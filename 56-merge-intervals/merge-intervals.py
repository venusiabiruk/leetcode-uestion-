class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        m = []
        intervals.sort(key = lambda i : i[0])
        for i in intervals:
            if not m or m[-1][1] < i[0]:
                m.append(i)
            else:
                m[-1] = [m[-1][0], max(m[-1][1],i[1])]
        return m 









        