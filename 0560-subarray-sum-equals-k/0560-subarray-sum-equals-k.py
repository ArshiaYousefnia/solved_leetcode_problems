class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        n = len(nums)
        count = 0
        hits = {0: 1}

        for i in range(n):
            sum += nums[i]
            count += hits.get(sum - k, 0)
            hits[sum] = hits.get(sum, 0) + 1

        return count 
                
