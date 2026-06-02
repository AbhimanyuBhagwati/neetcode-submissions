class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        area = 0

        def dfs(r: int, c:int) -> int:
            cnt =1
            if min(r, c) <0 or r == ROW or c ==COL or grid[r][c] ==0:
                return 0
            grid[r][c] =0

            cnt+=dfs(r, c+1)
            cnt+=dfs(r, c-1)
            cnt+=dfs(r-1, c)
            cnt+=dfs(r+1, c)
            return cnt
        

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] ==1:
                    _area = dfs(r,c)
                    if _area >= area:
                        area = _area
        return area
