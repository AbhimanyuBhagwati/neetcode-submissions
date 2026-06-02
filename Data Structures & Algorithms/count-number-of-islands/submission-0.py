class Solution:
    def numIslands(self, grid):
        ROWS, COLS = len(grid), len(grid[0])      # totals — caps

        def dfs(r, c):                            # r, c = current cell only
            if (min(r, c) < 0 or
                r == ROWS or c == COLS or         # blank 1, blank 2: off the edge?
                grid[r][c] == "0"):              # blank 3: not land?
                return
            # blank 4: what do you do to THIS cell so you never revisit it?
            grid[r][c] ="0"
            # (your flood-fill move — flip it)
            dfs(r, c+1)
            dfs(r,c-1)
            dfs(r-1, c)
            dfs(r+1, c)
        cnt = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] =='1':
                    dfs(r,c)
                    cnt+=1
        return cnt