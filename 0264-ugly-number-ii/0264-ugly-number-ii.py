import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = {1}
        
        for _ in range(n):
            b = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                nxt = b * factor
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)
        
        return b
