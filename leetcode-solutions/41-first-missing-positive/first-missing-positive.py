class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        uni=set(nums)
        i=1
        while i in uni:
            i+=1
        return i