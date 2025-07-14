class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        run_sum = nums[0]
        max_sum = run_sum

        for right in range(1, len(nums)):
            if run_sum < 0:
                run_sum = nums[right]
            else:
                run_sum += nums[right]
            
            max_sum = max(max_sum, run_sum)
        
        return max_sum


        