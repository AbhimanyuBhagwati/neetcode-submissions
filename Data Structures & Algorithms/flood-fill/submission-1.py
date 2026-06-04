#bfs
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        ROW, COL = len(image), len(image[0])
        org_color = image[sr][sc]
        queue = deque()
        image_copy = deepcopy(image)
        queue.append((sr,sc))
        while len(queue) >0:
            i,j = queue.popleft()
            image_copy[i][j] = color
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_x, new_y= x+i, y+j
                if new_x < 0 or new_x == ROW or new_y <0 or new_y == COL:
                    continue
                if image_copy[new_x][new_y] != org_color:
                    continue
                queue.append((new_x,new_y))
        return image_copy
