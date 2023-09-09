class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]

        def dfs(start,comb,total):
            if total==target:
                res.append(comb.copy())
                return
            if start>=len(candidates) or total>target:
                return
            
            comb.append(candidates[start])
            dfs(start,comb,total+candidates[start])
            comb.pop()
            dfs(start+1,comb,total)

        dfs(0,[],0)
        return res
