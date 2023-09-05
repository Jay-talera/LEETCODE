class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sal=[]
        sal[:]=salary[1:-1]
        res=sum(sal)/len(sal)
        # print(sal)
        return res