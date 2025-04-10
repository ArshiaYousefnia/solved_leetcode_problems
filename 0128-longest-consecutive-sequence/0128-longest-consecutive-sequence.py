class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        best = 0

        for i in a:
            if i - 1 in a:
                continue
            j = i + 1

            while j in a:
                j += 1
            
            best = max(best, j - i)
        
        return best

            




        