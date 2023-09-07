class Solution:
    def climbStairs(self, n: int) -> int:
        one,two=0,1
        while (n):
            one,two=two,one+two
            n-=1
        return two