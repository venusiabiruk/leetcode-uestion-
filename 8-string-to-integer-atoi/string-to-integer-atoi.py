class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Step 1: Remove leading and trailing whitespaces
        if not s:
            return 0

        sign = 1
        result = 0
        index = 0

        # Step 2: Check for sign
        if s[index] == '+' or s[index] == '-':
            sign = -1 if s[index] == '-' else 1
            index += 1

        # Step 3: Convert digits to a number
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1

        # Step 4: Clamp the result to 32-bit signed integer range
        result *= sign
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        # Step 5: Return the result
        return result
        