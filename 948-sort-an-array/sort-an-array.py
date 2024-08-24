from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr: List[int]) -> List[int]:
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left_half = merge_sort(arr[:mid])
            right_half = merge_sort(arr[mid:])
            
            return merge(left_half, right_half)
        
        def merge(left: List[int], right: List[int]) -> List[int]:
            sorted_list = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_list.append(left[i])
                    i += 1
                else:
                    sorted_list.append(right[j])
                    j += 1
            
            while i < len(left):
                sorted_list.append(left[i])
                i += 1
            
            while j < len(right):
                sorted_list.append(right[j])
                j += 1
            
            return sorted_list
        
        return merge_sort(nums)
