class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows,cols=len(grid),len(grid[0])
        islands=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j)
                    islands+=1
        return islands

    def dfs(self,grid,i,j):
        grid[i][j]=0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        for dr,dc in directions:
            r=i+dr
            c=j+dc
            if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c]=='1':
                self.dfs(grid,r,c)