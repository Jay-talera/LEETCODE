class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        left=0
        hm={}
        for index,val in enumerate(s):
            if val in hm:
                left=max(left,hm[val]+1)
            hm[val]=index
            res=max(res,index-left+1)
        return res