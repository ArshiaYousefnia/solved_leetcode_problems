class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(
            self.linear_rob(nums[:-1]),
            self.linear_rob(nums[1:])
        )

    def linear_rob(self, nums: list[int]) -> int:
        prev2 = 0
        prev1 = 0

        for x in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + x)

        return prev1