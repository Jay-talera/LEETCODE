class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]

        def dfs(total,comb,start):
            if total==target:
                res.append(comb[:])
                return
            if total>target or start>=len(candidates):
                return
            
            for i in range(start,len(candidates)):
                comb.append(candidates[i])
                dfs(total+candidates[i],comb,i)
                comb.pop()
        dfs(0,[],0)
        return res
