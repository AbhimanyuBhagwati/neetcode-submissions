import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        _heap = []
        for i in range(len(stones)):
            heapq.heappush(_heap , -stones[i])

        while len(_heap)>1:
            frst_s, snd_s = abs(heapq.heappop(_heap)),abs(heapq.heappop(_heap))
            _rem = frst_s - snd_s
            if _rem > 0:
                heapq.heappush(_heap, -_rem)
            


        if _heap: 
            return abs(_heap[0])
        return 0