class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        s = set()
        for i in nums1:
            if i in nums2:
                s.add(i)
        return s



        