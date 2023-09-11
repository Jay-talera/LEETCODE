class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res=[]
        res.append(set(nums1)-set(nums2))
        res.append(set(nums2)-set(nums1))
        return res