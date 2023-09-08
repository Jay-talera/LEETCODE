class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pa(s:str,l:int,r:int):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l -=1
                r +=1
            return s[l+1:r]
        p=''
        for i in range (len(s)):
            p1=pa(s,i,i+1)
            p2=pa(s,i,i)
            p=max(p,p1,p2,key=len)
        return p