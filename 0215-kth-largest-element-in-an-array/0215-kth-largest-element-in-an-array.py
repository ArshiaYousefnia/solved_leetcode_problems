import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a = []
        n = 0
        for i in nums:
            heapq.heappush(a, i)
            n += 1
            if n > k:
                heapq.heappop(a)
                n -= 1
        
        return heapq.heappop(a)
        