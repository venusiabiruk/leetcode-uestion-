class Solution:
    def isValid(self, s: str) -> bool:
        map = {")":"(","}":"{","]":"["}
        st = []
        for c in s:
            if c not in map:
                st.append(c)
            else:
                if not st:
                    return False
                else:
                    popped = st.pop()
                    if popped != map[c]:
                        return False
        return not st




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        stack = []
        matching_bracket = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in matching_bracket:
                top_element = stack.pop() if stack else '#'
                
                if matching_bracket[char] != top_element:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0

