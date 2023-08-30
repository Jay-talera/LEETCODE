class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ops = 0
        prev = inf
        for num in reversed(nums):
            if num > prev:
                times = (num + prev - 1) // prev
                prev = num // times
                ops += times - 1
            else:
                prev = num
        return ops