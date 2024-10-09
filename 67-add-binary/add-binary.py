class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1

            carry = total // 2  # Calculate new carry
            result.append(str(total % 2))  # Append the sum of bits

        return ''.join(result[::-1])  # Reverse and join the res

        

        