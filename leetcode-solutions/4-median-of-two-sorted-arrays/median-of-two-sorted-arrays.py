class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1)%2==1:
            s=(len(nums1)//2)
            return nums1[s]
        else:
            s=(len(nums1)//2)
            return (nums1[s]+nums1[s-1])/2