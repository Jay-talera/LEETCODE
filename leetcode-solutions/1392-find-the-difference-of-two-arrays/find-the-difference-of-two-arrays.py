class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1=set(nums1)
        tmp=s1
        s2=set(nums2)
        s1=s1-s2
        s2=s2-tmp
        # print(list(s1))
        # print(list(s2))
        res=[]
        res.append(list(s1))
        res.append(list(s2))
        return res