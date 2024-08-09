class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
                
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []
        
        
        while i >= 0 or j >= 0 or carry:
            
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            
            # Calculate sum of current digits plus carry
            total = digit1 + digit2 + carry
            
            # Determine new carry and digit to add to result
            carry = total // 10
            result.append(total % 10)
            
            # Move to the next digits
            i -= 1
            j -= 1
        
        # Reverse the result list and convert to string
        return ''.join(map(str, result[::-1]))

    