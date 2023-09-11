class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups={}
        res=[]

        for ind , val in enumerate(groupSizes):
            groups[val] = groups.get(val,[])+[ind]
            if len(groups[val])==val:
                res.append(groups[val])
                groups[val]=[]
        return res