class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        a = {}
        n = 0

        for num in nums:
            if num <= 0:
                continue
            
            a[num] = 1
            n += 1
        
        out = 1

        for i in range(1, n + 1):
            if a.get(out, 0) == 1:
                out += 1
                continue
            break
        
        return out
        