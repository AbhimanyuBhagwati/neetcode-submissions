import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        _heap = []
        for x,y in points:
            _dis = (x)**2+(y)**2
            heapq.heappush(_heap,(_dis, [x,y]))

        
        _temp = []

        for i in range(k):
            _val , pnt = heapq.heappop(_heap)
            _temp.append(pnt)
        return _temp
