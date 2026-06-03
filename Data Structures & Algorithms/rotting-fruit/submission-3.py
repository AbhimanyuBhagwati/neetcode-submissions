class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        fresh_count = 0
        queue= deque()
        grid_copy = deepcopy(grid)
        for r in range(ROW):
            for c in range(COL):
                if grid_copy[r][c] == 2:
                    queue.append((r, c))
                elif grid_copy[r][c] == 1:
                    fresh_count +=1
        
        min = 0
        while fresh_count > 0 and len(queue) !=0:
            min+=1
            tot_rttn = len(queue)
            for _ in range(tot_rttn):
                r,c = queue.popleft()
                for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                    new_x, new_y = r+x , c+y
                    if new_x< 0 or new_y <0 or new_x == ROW or new_y == COL :
                        continue
                    if grid_copy[new_x][new_y] ==2 or grid_copy[new_x][new_y] == 0:
                        continue
                    fresh_count -=1
                    grid_copy[new_x][new_y] = 2
                    queue.append((new_x, new_y))
        if fresh_count>0:
            return -1
        return min