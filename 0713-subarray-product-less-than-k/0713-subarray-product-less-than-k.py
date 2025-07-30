class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        prod = 1
        count = 0
        i = 0
        j = 0

        for j in range(len(nums)):
            prod *= nums[j]

            while prod >= k and i < j:
                prod /= nums[i]

                i += 1
            
            if prod < k:
                count += j - i + 1
        
        return count
        