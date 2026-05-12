class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = []
        k = celsius+273.15
        F = celsius * 1.80 + 32.00
        ans.append(k)
        ans.append(F)
        return ans 
        