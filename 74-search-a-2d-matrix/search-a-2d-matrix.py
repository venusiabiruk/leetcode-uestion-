class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Check if the matrix is empty
        m = len(matrix)
        if m == 0:
            return False
        
        n = len(matrix[0])
        if n == 0:
            return False
        
        # Find the row to search in using binary search
        low, high = 0, m - 1
        
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                # Target is within this row's range
                lm = matrix[mid]
                break
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # If no valid row found
            return False
        
        # Search for the target in the selected row
        low, high = 0, len(lm) - 1
        while low <= high:
            mid = (low + high) // 2
            if lm[mid] == target:
                return True
            elif lm[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
