class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # The prefix to be returned
        prefix = ""
        
        # Iterate over the characters of the first string
        for i in range(len(strs[0])):
            # Get the character from the first string
            char = strs[0][i]
            
            # Check if this character is present at the same position in all strings
            for string in strs:
                if i >= len(string) or string[i] != char:
                    return prefix
            
            # If all strings have the same character at this index, add it to prefix
            prefix += char
        
        return prefix
        