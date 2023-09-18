class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        arr = []
        for r in range(len(mat)):
            total = 0
            for c in range(len(mat[r])):
                total += mat[r][c]
            arr.append([total,r])
        
        heapq.heapify(arr)

        res = []
        while k > 0:
            _,row = heapq.heappop(arr)
            res.append(row)
            k-=1
        return res

        