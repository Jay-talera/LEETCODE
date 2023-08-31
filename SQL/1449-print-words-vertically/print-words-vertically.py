class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr=s.split()
        maxlen=len(max(arr,key=len))
        res=[""]*maxlen
        for word in arr:
            for i in range(0,len(res)):
                if i<len(word):
                    res[i]+=word[i]
                else:
                    res[i]+=' '
        solution=[]
        for word in res:
            solution.append(word.rstrip())
        return solution