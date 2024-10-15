class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            partition1 = (low + high) // 2
            partition2 = (m + n + 1) // 2 - partition1
            
            # Set maxLeft and minRight for partition1
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            # Set maxLeft and minRight for partition2
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we have found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # We have partitioned the array correctly
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                # We are too far on the right side for partition1. Go left.
                high = partition1 - 1
            else:
                # We are too far on the left side for partition1. Go right.
                low = partition1 + 1
        
        raise ValueError("Input arrays are not sorted or valid.")

        